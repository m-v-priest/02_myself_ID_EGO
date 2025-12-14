// timeline.js

document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------------------
    // 0. DOM 元素获取 (保持不变)
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

    // ----------------------------------------------------------------
    // 1. 全局配置、默认值 与 localStorage加载 (保持不变)
    // ----------------------------------------------------------------
    let eventData = {};
    const YEAR_INTERVAL_NORMAL = 100;
    const YEAR_INTERVAL_FINE = 10;
    const FINE_GRAIN_START_YEAR = 1800;
    const YEAR_SPACING_UNIT = 50;

    const MODERN_START_YEAR = 1900;
    const DEFAULT_MODERN_ZOOM = 2.0;

    const DEFAULT_ZOOM = 1.0;
    const DEFAULT_FONT_SIZE = 12;
    const DEFAULT_DOT_SIZE = 4;
    const DEFAULT_MIN_YEAR = -300;
    const DEFAULT_MAX_YEAR = 1000;

    let currentZoom = parseFloat(localStorage.getItem('timelineZoom')) || DEFAULT_ZOOM;
    let currentMinYear = parseInt(localStorage.getItem('timelineMinYear')) || DEFAULT_MIN_YEAR;
    let currentMaxYear = parseInt(localStorage.getItem('timelineMaxYear')) || DEFAULT_MAX_YEAR;
    let currentModernZoomFactor = parseFloat(localStorage.getItem('modernZoomFactor')) || DEFAULT_MODERN_ZOOM;

    minYearInput.value = currentMinYear;
    maxYearInput.value = currentMaxYear;
    fontSizeInput.value = parseInt(localStorage.getItem('timelineFontSize')) || DEFAULT_FONT_SIZE;
    dotSizeInput.value = parseInt(localStorage.getItem('timelineDotSize')) || DEFAULT_DOT_SIZE;
    modernZoomInput.value = currentModernZoomFactor;

    let maxRequiredXEver = 0;


    // ... (loadData 和 wrapText 函数 保持不变) ...
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

        return lines.slice(0, 5);
    }

    // ----------------------------------------------------------------
    // 3. 核心绘图函数 (drawTimeline) - 关键修改在这里
    // ----------------------------------------------------------------

    function drawTimeline() {
        svg.innerHTML = '';

        // --- 核心配置 ---
        const baseFontSize = parseInt(fontSizeInput.value); // 用户设定的基础字号
        const dotSize = parseInt(dotSizeInput.value);
        const axisX = 100;
        const X_OFFSET = 10;
        const PADDING = 40;
        const containerWidth = container.offsetWidth;

        // ⭐ 新增：主刻度字号比基础字号大 10px
        const majorTickFontSize = baseFontSize + 10;

        const spacingAncient = YEAR_SPACING_UNIT * currentZoom;
        const spacingModern = spacingAncient * currentModernZoomFactor;

        // --- 动态 Y 坐标计算函数 (保持不变) ---
        function getYPos(year) {
            if (year < MODERN_START_YEAR) {
                return (year - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
            } else {
                const yPosAncientEnd = (MODERN_START_YEAR - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
                return yPosAncientEnd + (year - MODERN_START_YEAR) / YEAR_INTERVAL_NORMAL * spacingModern;
            }
        }

        // --- 动态计算 SVG 总高度 (保持不变) ---
        let svgHeight;
        if (currentMaxYear < MODERN_START_YEAR) {
            svgHeight = (currentMaxYear - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient + 100;
        } else {
            const heightAncient = (MODERN_START_YEAR - currentMinYear) / YEAR_INTERVAL_NORMAL * spacingAncient;
            const heightModern = (currentMaxYear - MODERN_START_YEAR) / YEAR_INTERVAL_NORMAL * spacingModern;
            svgHeight = heightAncient + heightModern + 100;
        }


        // --- 换行宽度设置 (保持不变) ---
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

        // --- 绘制刻度线和年份标签子函数 (关键修改在这里) ---
        function drawTick(year, interval) {
            const yPos = getYPos(year);
            const tickLength = (interval === YEAR_INTERVAL_NORMAL) ? 10 : 5;

            if (yPos > svgHeight) return;

            const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            tick.setAttribute('x1', axisX - tickLength);
            tick.setAttribute('y1', yPos);
            tick.setAttribute('x2', axisX + tickLength);
            tick.setAttribute('y2', yPos);
            tick.setAttribute('stroke', 'black');
            tick.setAttribute('stroke-width', 1);
            svg.appendChild(tick);

            // 判断是否是主要刻度（100年间隔）
            const isMajorTickLabel = (year % YEAR_INTERVAL_NORMAL === 0);

            // 判断是否是细分刻度（10年间隔，且不是100年间隔）
            const isMinorTickLabel = (year >= FINE_GRAIN_START_YEAR && year % YEAR_INTERVAL_FINE === 0 && year % YEAR_INTERVAL_NORMAL !== 0);

            if (isMajorTickLabel || isMinorTickLabel) {
                const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                const labelXOffset = (tickLength + 5);

                label.setAttribute('x', axisX - labelXOffset);
                label.setAttribute('y', yPos + (baseFontSize / 3));
                label.setAttribute('text-anchor', 'end');

                // ⭐ 关键修改：根据是否是主刻度来设置字号
                let currentFontSize = isMajorTickLabel ? majorTickFontSize : baseFontSize;
                label.setAttribute('font-size', currentFontSize);

                // 颜色区分 (保持不变)
                if (isMinorTickLabel) {
                    label.setAttribute('fill', 'green');
                } else {
                    label.setAttribute('fill', 'black');
                }

                label.textContent = year >= 0 ? year + '年' : '前' + Math.abs(year) + '年';
                svg.appendChild(label);
            }
        }

        // --- 绘制间隔线和年份标签 (保持不变) ---
        for (let year = currentMinYear; year <= currentMaxYear; year += YEAR_INTERVAL_FINE) {
            if (year % YEAR_INTERVAL_FINE === 0 || year % YEAR_INTERVAL_NORMAL === 0) {
                 drawTick(year, year >= FINE_GRAIN_START_YEAR && year % YEAR_INTERVAL_NORMAL !== 0 ? YEAR_INTERVAL_FINE : YEAR_INTERVAL_NORMAL);
            }
        }


        // --- 绘制历史事件点和说明 (保持不变) ---
        let currentYOffset = 0;

        const sortedEvents = Object.keys(eventData).sort((a, b) => Number(a) - Number(b));

        sortedEvents.forEach(yearStr => {
            const year = Number(yearStr);
            const [description, color] = eventData[yearStr];

            if (year > currentMaxYear || year < currentMinYear) return;

            const yPos = getYPos(year);

            // 1. 分割文本并计算多行高度
            const parts = description.split(' / ');
            const yearText = parts[0];
            const eventDesc = parts.length > 1 ? parts.slice(1).join(' / ') : parts[0];
            const fullText = yearText + ' / ' + eventDesc;

            const textLines = wrapText(fullText, currentMaxWidth, baseFontSize);
            const totalTextHeight = textLines.length * (baseFontSize + 3);

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

            // 3. 绘制圆点
            const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dot.setAttribute('cx', axisX);
            dot.setAttribute('cy', yPos);
            dot.setAttribute('r', dotSize);
            dot.setAttribute('fill', color || 'black');
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
            textElement.setAttribute('y', newYOffsetStart + (baseFontSize / 3));
            textElement.setAttribute('font-size', baseFontSize); // 使用基础字号
            textElement.setAttribute('fill', color || 'black');

            textLines.forEach((line, index) => {
                const tspan = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
                tspan.setAttribute('x', axisX + X_OFFSET * 2);
                tspan.setAttribute('dy', (index === 0 ? 0 : baseFontSize + 3));
                tspan.textContent = line;
                textElement.appendChild(tspan);
            });

            svg.appendChild(textElement);

            finalYMax = Math.max(finalYMax, currentYOffset);
        });

        // --- 最终更新 SVG 宽度和高度 (保持不变) ---
        if (requiredMaxX > maxRequiredXEver) {
            maxRequiredXEver = requiredMaxX;
        }

        svg.setAttribute('width', maxRequiredXEver + 'px');
        svg.setAttribute('height', finalYMax + 50 + 'px');
        mainLine.setAttribute('y2', finalYMax + 50);
    }

    // ----------------------------------------------------------------
    // 4. 交互功能 (保持不变)
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

    modernZoomInput.addEventListener('change', () => {
        handleUpdate();
    });

    fontSizeInput.addEventListener('change', () => {
        localStorage.setItem('timelineFontSize', fontSizeInput.value);
        maxRequiredXEver = 0;
        drawTimeline();
    });
    dotSizeInput.addEventListener('change', () => {
        localStorage.setItem('timelineDotSize', dotSizeInput.value);
        drawTimeline();
    });
    updateBtn.addEventListener('click', handleUpdate);

    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(drawTimeline, 200);
    });

    loadData();
});