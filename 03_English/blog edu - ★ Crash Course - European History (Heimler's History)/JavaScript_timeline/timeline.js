// timeline.js

document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------------------
    // 0. DOM 元素获取
    // ----------------------------------------------------------------
    const svg = document.getElementById('timeline-svg');
    const container = document.getElementById('timeline-container');
    const zoomInBtn = document.getElementById('zoom-in');
    const zoomOutBtn = document.getElementById('zoom-out');
    const updateBtn = document.getElementById('update-timeline');
    const minYearInput = document.getElementById('min-year');
    const maxYearInput = document.getElementById('max-year');
    const fontSizeInput = document.getElementById('font-size');
    const dotSizeInput = document.getElementById('dot-size');
    const modernZoomInput = document.getElementById('modern-zoom');

    // 获取快速定位链接的容器
    const quickJumpLinksDiv = document.getElementById('quick-jump-links');


    // ----------------------------------------------------------------
    // 1. 全局配置、默认值 与 localStorage加载
    // ----------------------------------------------------------------
    let eventData = {}; // 用于存储 data.json 中的事件数据
    const YEAR_INTERVAL_NORMAL = 100; // 主刻度间隔
    const YEAR_INTERVAL_FINE = 10;    // 细刻度间隔
    const FINE_GRAIN_START_YEAR = 1800; // 细刻度开始年份
    const YEAR_SPACING_UNIT = 50;     // 默认缩放下的每 100 年像素单位

    const MODERN_START_YEAR = 1800; // 近代开始年份
    const DEFAULT_MODERN_ZOOM = 2.0;

    const DEFAULT_ZOOM = 1.0;
    const DEFAULT_FONT_SIZE = 12;
    const DEFAULT_DOT_SIZE = 4;
    const DEFAULT_MIN_YEAR = -300;
    const DEFAULT_MAX_YEAR = 1000;

    // 从 localStorage 加载或使用默认值
    let currentZoom = parseFloat(localStorage.getItem('timelineZoom')) || DEFAULT_ZOOM;
    let currentMinYear = parseInt(localStorage.getItem('timelineMinYear')) || DEFAULT_MIN_YEAR;
    let currentMaxYear = parseInt(localStorage.getItem('timelineMaxYear')) || DEFAULT_MAX_YEAR;
    let currentModernZoomFactor = parseFloat(localStorage.getItem('modernZoomFactor')) || DEFAULT_MODERN_ZOOM;

    minYearInput.value = currentMinYear;
    maxYearInput.value = currentMaxYear;
    fontSizeInput.value = parseInt(localStorage.getItem('timelineFontSize')) || DEFAULT_FONT_SIZE;
    dotSizeInput.value = parseInt(localStorage.getItem('timelineDotSize')) || DEFAULT_DOT_SIZE;
    modernZoomInput.value = currentModernZoomFactor;

    let maxRequiredXEver = 0; // 记录事件文本最右边界


    // ----------------------------------------------------------------
    // 辅助函数
    // ----------------------------------------------------------------
    async function loadData() {
        try {
            const response = await fetch('data.json');
            if (!response.ok) {
                throw new Error(`无法获取 data.json。状态码: ${response.status}。请确认文件是否存在并检查网络。`);
            }
            eventData = await response.json();
            if (Object.keys(eventData).length === 0) {
                container.innerHTML = '<p style="color: orange; text-align: center;">警告：data.json 文件已加载，但其中没有事件数据。</p>';
                return;
            }
            drawTimeline();
        } catch (error) {
            console.error('加载 JSON 数据时出错:', error);
            container.innerHTML = `
                <div style="color: red; padding: 20px; text-align: center;">
                    <h2>数据加载失败！</h2>
                    <p>错误信息: ${error.message}</p>
                    <p>解决办法：请在本地启动一个 Web 服务器（例如 Live Server）再访问页面。</p>
                </div>
            `;
        }
    }

    function wrapText(text, maxWidth, fontSize) {
        if (!text || text.length === 0) return [""];
        if (maxWidth <= 0) return [text];

        const lines = [];
        let currentLine = '';

        const CHAR_WIDTH_APPROX = fontSize * 1.05;
        const maxCharsPerLine = Math.floor(maxWidth / CHAR_WIDTH_APPROX);

        if (text.length <= maxCharsPerLine) {
            return [text];
        }

        let words = Array.from(text);

        for (let i = 0; i < words.length; i++) {
            const char = words[i];

            if ((currentLine.length + 1) * CHAR_WIDTH_APPROX > maxWidth && currentLine.length > 0) {
                lines.push(currentLine);
                currentLine = char;
            } else {
                currentLine += char;
            }
        }

        if (currentLine.length > 0) {
            lines.push(currentLine);
        }

        return lines.slice(0, 5); // 最多只显示 5 行
    }


    // ----------------------------------------------------------------
    // 2. 导航链接生成函数
    // ----------------------------------------------------------------
    function createYearJumpLinks() {
        quickJumpLinksDiv.innerHTML = '';
        const fragment = document.createDocumentFragment();

        // 滚动时的偏移量，确保目标年份显示在容器顶部下方 50px 处
        const SCROLL_OFFSET = 50;

        // 遍历所有 100 年的整数倍年份
        for (let year = currentMinYear; year <= currentMaxYear; year += YEAR_INTERVAL_NORMAL) {

            if (year % YEAR_INTERVAL_NORMAL !== 0) continue;

            const yearDisplay = year >= 0 ? year.toString() : '前' + Math.abs(year);
            const link = document.createElement('a');

            // 链接的 href 指向 SVG 元素上的唯一 ID 锚点
            link.href = '#year-label-' + year;
            link.textContent = yearDisplay + '年';

            // 修复后的点击事件滚动逻辑
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    // 获取 SVG text 元素相对于 SVG 自身的 Y 坐标
                    const targetY = parseFloat(targetElement.getAttribute('y'));

                    // 计算滚动到 timeline-container 的目标位置
                    const targetScrollTop = Math.max(0, targetY - SCROLL_OFFSET);

                    container.scrollTo({
                        top: targetScrollTop,
                        behavior: 'smooth'
                    });
                } else {
                    console.warn(`未找到目标年份元素: ${targetId}。请检查 drawTimeline 函数是否为该年份设置了正确的 ID。`);
                }
            });

            fragment.appendChild(link);
        }

        quickJumpLinksDiv.appendChild(fragment);
    }


    // ----------------------------------------------------------------
    // 3. 核心绘图函数 (drawTimeline)
    // ----------------------------------------------------------------
    function drawTimeline() {
        svg.innerHTML = '';

        // --- 核心配置 ---
        const baseFontSize = parseInt(fontSizeInput.value);
        const dotSize = parseInt(dotSizeInput.value);
        const axisX = 100; // 时间轴线的 X 坐标
        const X_OFFSET = 10; // 文本与时间轴线之间的间隔
        const PADDING = 40;
        const containerWidth = container.offsetWidth;

        const majorTickFontSize = baseFontSize + 10;

        const spacingAncient = YEAR_SPACING_UNIT * currentZoom;
        const spacingModern = spacingAncient * currentModernZoomFactor;

        // --- 动态 Y 坐标计算函数 ---
        function getYPos(year) {
            if (year < MODERN_START_YEAR) {
                // 古代部分
                return (year - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
            } else {
                // 近代部分 (应用放大倍数)
                const yPosAncientEnd = (MODERN_START_YEAR - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
                return yPosAncientEnd + (year - MODERN_START_YEAR) / YEAR_INTERVAL_NORMAL * spacingModern;
            }
        }

        // --- 动态计算 SVG 总高度 ---
        let svgHeight;
        if (currentMaxYear < MODERN_START_YEAR) {
            svgHeight = (currentMaxYear - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient + 100;
        } else {
            const heightAncient = (MODERN_START_YEAR - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
            const heightModern = (currentMaxYear - MODERN_START_YEAR) / YEAR_INTERVAL_NORMAL * spacingModern;
            svgHeight = heightAncient + heightModern + 100;
        }

        // --- 换行宽度设置 ---
        const MIN_SAFE_TEXT_WIDTH = 300;
        let currentMaxWidth = containerWidth - axisX - (X_OFFSET * 2) - PADDING;

        if (currentMaxWidth < MIN_SAFE_TEXT_WIDTH) {
            currentMaxWidth = MIN_SAFE_TEXT_WIDTH;
        }

        // --- 绘图变量 ---
        let finalYMax = 0;
        let requiredMaxX = 0;


        // --- 绘制主时间轴线 ---
        const mainLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        mainLine.setAttribute('x1', axisX);
        mainLine.setAttribute('y1', 0);
        mainLine.setAttribute('x2', axisX);
        mainLine.setAttribute('y2', svgHeight);
        mainLine.setAttribute('stroke', 'black');
        mainLine.setAttribute('stroke-width', 2);
        svg.appendChild(mainLine);

        // --- 绘制刻度线和年份标签子函数 ---
        function drawTick(year, interval) {
            const yPos = getYPos(year);
            const tickLength = (interval === YEAR_INTERVAL_NORMAL) ? 10 : 5;

            if (yPos > svgHeight) return;

            // 绘制刻度线
            const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            tick.setAttribute('x1', axisX - tickLength);
            tick.setAttribute('y1', yPos);
            tick.setAttribute('x2', axisX + tickLength);
            tick.setAttribute('y2', yPos);
            tick.setAttribute('stroke', 'black');
            tick.setAttribute('stroke-width', 1);
            svg.appendChild(tick);

            const isMajorTickLabel = (year % YEAR_INTERVAL_NORMAL === 0);
            const isMinorTickLabel = (year >= FINE_GRAIN_START_YEAR && year % YEAR_INTERVAL_FINE === 0 && year % YEAR_INTERVAL_NORMAL !== 0);

            if (isMajorTickLabel || isMinorTickLabel) {
                // 绘制年份标签
                const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                const labelXOffset = (tickLength + 5);

                label.setAttribute('x', axisX - labelXOffset);
                label.setAttribute('y', yPos + (baseFontSize / 3));
                label.setAttribute('text-anchor', 'end');

                let currentFontSize = isMajorTickLabel ? majorTickFontSize : baseFontSize;
                label.setAttribute('font-size', currentFontSize);

                if (isMinorTickLabel) {
                    label.setAttribute('fill', 'green');
                } else {
                    label.setAttribute('fill', 'black');
                }

                label.textContent = year >= 0 ? year + '年' : '前' + Math.abs(year) + '年';

                // ⭐ 关键：为 100 年间隔的标签添加唯一的 ID (锚点)
                if (isMajorTickLabel) {
                     label.setAttribute('id', 'year-label-' + year);
                }

                svg.appendChild(label);
            }
        }

        // --- 绘制所有刻度 ---
        for (let year = currentMinYear; year <= currentMaxYear; year += YEAR_INTERVAL_FINE) {
            if (year % YEAR_INTERVAL_FINE === 0 || year % YEAR_INTERVAL_NORMAL === 0) {
                 drawTick(year, year >= FINE_GRAIN_START_YEAR && year % YEAR_INTERVAL_NORMAL !== 0 ? YEAR_INTERVAL_FINE : YEAR_INTERVAL_NORMAL);
            }
        }

        // ⭐ 关键：在绘制时间轴后，生成导航链接
        createYearJumpLinks();


        // --- 绘制历史事件点和说明 ---
        let currentYOffset = 0;

        const sortedEvents = Object.keys(eventData).sort((a, b) => Number(a) - Number(b));

        sortedEvents.forEach(yearStr => {
            const year = Number(yearStr);
            const eventDetails = eventData[yearStr];

            if (!eventDetails || eventDetails.length < 2) return;

            const description = eventDetails[0];
            const dotColor = eventDetails[1] || 'black';
            const textBgColor = eventDetails[2];
            const fontSizeDelta = eventDetails[3] || 0;


            if (year > currentMaxYear || year < currentMinYear) return;

            const yPos = getYPos(year);

            const eventFontSize = baseFontSize + fontSizeDelta;

            // 1. 分割文本并计算多行高度
            const parts = description.split(' / ');
            const yearText = parts[0];
            const eventDesc = parts.length > 1 ? parts.slice(1).join(' / ') : parts[0];
            const fullText = yearText + ' / ' + eventDesc;

            const textLines = wrapText(fullText, currentMaxWidth, eventFontSize);
            const totalTextHeight = textLines.length * (eventFontSize + 3);

            // 估算文本块的理论最右边界 X 坐标
            const textXEnd = axisX + (X_OFFSET * 2) + currentMaxWidth + (PADDING / 2);
            requiredMaxX = Math.max(requiredMaxX, textXEnd);

            // 2. 错位逻辑
            let newYOffsetStart;
            if (yPos < currentYOffset) {
                newYOffsetStart = currentYOffset;
            } else {
                newYOffsetStart = yPos;
            }

            const textYBottom = newYOffsetStart + totalTextHeight;
            currentYOffset = textYBottom + 5;

            // --- 绘制背景矩形 ---
            if (textBgColor && textBgColor !== 'null') {
                const backgroundRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
                backgroundRect.setAttribute('x', axisX + X_OFFSET * 2 - 2);
                backgroundRect.setAttribute('y', newYOffsetStart - eventFontSize + 1);
                backgroundRect.setAttribute('width', currentMaxWidth + 4);
                backgroundRect.setAttribute('height', totalTextHeight + 4);
                backgroundRect.setAttribute('fill', textBgColor);
                backgroundRect.setAttribute('opacity', 0.8);
                svg.appendChild(backgroundRect);
            }

            // 3. 绘制圆点
            const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dot.setAttribute('cx', axisX);
            dot.setAttribute('cy', yPos);
            dot.setAttribute('r', dotSize);
            dot.setAttribute('fill', dotColor);
            svg.appendChild(dot);

            // 4. 绘制指向文本起始点的箭头线
            const lineToText = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            lineToText.setAttribute('x1', axisX);
            lineToText.setAttribute('y1', yPos);
            lineToText.setAttribute('x2', axisX + X_OFFSET + 5);
            lineToText.setAttribute('y2', newYOffsetStart);
            lineToText.setAttribute('stroke', 'gray');
            lineToText.setAttribute('stroke-width', 1);
            svg.appendChild(lineToText);

            // 5. 绘制多行文本
            const textElement = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            textElement.setAttribute('x', axisX + X_OFFSET * 2);
            textElement.setAttribute('y', newYOffsetStart + (eventFontSize / 3));

            textElement.setAttribute('font-size', eventFontSize);
            textElement.setAttribute('fill', dotColor);

            textLines.forEach((line, index) => {
                const tspan = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
                tspan.setAttribute('x', axisX + X_OFFSET * 2);
                tspan.setAttribute('dy', (index === 0 ? 0 : eventFontSize + 3));
                tspan.textContent = line;
                textElement.appendChild(tspan);
            });

            svg.appendChild(textElement);

            finalYMax = Math.max(finalYMax, currentYOffset);
        });

        // --- 最终更新 SVG 宽度和高度 ---
        if (requiredMaxX > maxRequiredXEver) {
            maxRequiredXEver = requiredMaxX;
        }

        svg.setAttribute('width', maxRequiredXEver + 'px');
        svg.setAttribute('height', finalYMax + 50 + 'px');
        mainLine.setAttribute('y2', finalYMax + 50);
    }

    // ----------------------------------------------------------------
    // 4. 交互功能
    // ----------------------------------------------------------------

    function handleZoom(factor) {
        currentZoom = Math.max(0.5, currentZoom * factor);
        currentZoom = Math.min(50.0, currentZoom);
        localStorage.setItem('timelineZoom', currentZoom.toFixed(2));
        maxRequiredXEver = 0;
        drawTimeline();
    }

    function handleUpdate() {
        let newMinYear = parseInt(minYearInput.value);
        let newMaxYear = parseInt(maxYearInput.value);
        let newModernZoom = parseFloat(modernZoomInput.value);

        if (newMaxYear <= newMinYear) {
             alert("最大年份必须大于起始年份！");
             return;
        }
        if (newModernZoom < 1.0) {
             alert("近代放大倍数 n 必须大于或等于 1.0！");
             modernZoomInput.value = currentModernZoomFactor;
             return;
        }

        // 规范化年份到 100 的倍数
        if (newMinYear % YEAR_INTERVAL_NORMAL !== 0) {
            newMinYear = Math.floor(newMinYear / YEAR_INTERVAL_NORMAL) * YEAR_INTERVAL_NORMAL;
            minYearInput.value = newMinYear;
        }

        if (newMaxYear % YEAR_INTERVAL_NORMAL !== 0) {
            newMaxYear = Math.ceil(newMaxYear / YEAR_INTERVAL_NORMAL) * YEAR_INTERVAL_NORMAL;
            maxYearInput.value = newMaxYear;
        }

        currentMinYear = newMinYear;
        currentMaxYear = newMaxYear;
        currentModernZoomFactor = newModernZoom;

        localStorage.setItem('timelineMinYear', currentMinYear);
        localStorage.setItem('timelineMaxYear', currentMaxYear);
        localStorage.setItem('modernZoomFactor', currentModernZoomFactor.toFixed(1));

        maxRequiredXEver = 0;
        drawTimeline();
    }

    zoomInBtn.addEventListener('click', () => handleZoom(1.2));
    zoomOutBtn.addEventListener('click', () => handleZoom(1 / 1.2));
    modernZoomInput.addEventListener('change', handleUpdate);
    fontSizeInput.addEventListener('change', handleUpdate);
    dotSizeInput.addEventListener('change', drawTimeline);
    updateBtn.addEventListener('click', handleUpdate);

    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(drawTimeline, 200);
    });

    // 页面加载完成后启动
    loadData();
});