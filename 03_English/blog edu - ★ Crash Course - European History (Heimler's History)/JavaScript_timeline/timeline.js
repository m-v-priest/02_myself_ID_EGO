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

    // ----------------------------------------------------------------
    // 1. 全局配置、默认值 与 localStorage加载
    // ----------------------------------------------------------------
    let eventData = {}; // 存储 JSON 数据
    const YEAR_INTERVAL_NORMAL = 100; // 基础间隔：100年
    const YEAR_INTERVAL_FINE = 10;   // 精细间隔：10年
    const FINE_GRAIN_START_YEAR = 1800; // 切换到 10 年间隔的年份
    const YEAR_SPACING_UNIT = 50; // SVG中每100年对应的像素高度（作为缩放基准）

    // 定义默认值
    const DEFAULT_ZOOM = 1.0;
    const DEFAULT_FONT_SIZE = 12;
    const DEFAULT_DOT_SIZE = 4;
    const DEFAULT_MIN_YEAR = -300;
    const DEFAULT_MAX_YEAR = 1000;

    // 从 localStorage 加载参数，如果没有则使用默认值
    let currentZoom = parseFloat(localStorage.getItem('timelineZoom')) || DEFAULT_ZOOM;
    let currentMinYear = parseInt(localStorage.getItem('timelineMinYear')) || DEFAULT_MIN_YEAR;
    let currentMaxYear = parseInt(localStorage.getItem('timelineMaxYear')) || DEFAULT_MAX_YEAR;

    // 将加载的参数应用到输入框，覆盖 HTML 中的默认值
    minYearInput.value = currentMinYear;
    maxYearInput.value = currentMaxYear;
    fontSizeInput.value = parseInt(localStorage.getItem('timelineFontSize')) || DEFAULT_FONT_SIZE;
    dotSizeInput.value = parseInt(localStorage.getItem('timelineDotSize')) || DEFAULT_DOT_SIZE;


    // ----------------------------------------------------------------
    // 2. 数据加载函数
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

    // ----------------------------------------------------------------
    // 3. 核心绘图函数 (使用 SVG)
    // ----------------------------------------------------------------
    function drawTimeline() {
        // 清空旧的SVG内容
        svg.innerHTML = '';

        // --- 参数获取 ---
        const fontSize = parseInt(fontSizeInput.value);
        const dotSize = parseInt(dotSizeInput.value);
        const spacing = YEAR_SPACING_UNIT * currentZoom;

        const minYearToDraw = currentMinYear;

        // 计算 SVG 的总高度（Y轴表示年份）
        let totalYears = currentMaxYear - minYearToDraw;
        const svgHeight = (totalYears / YEAR_INTERVAL_NORMAL) * spacing + 50;
        svg.setAttribute('height', svgHeight + 'px');

        const axisX = 100; // 时间轴垂直线所在的 X 坐标

        // --- 绘制主时间轴线 ---
        const mainLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        mainLine.setAttribute('x1', axisX);
        mainLine.setAttribute('y1', 0);
        mainLine.setAttribute('x2', axisX);
        mainLine.setAttribute('y2', svgHeight);
        mainLine.setAttribute('stroke', 'black');
        mainLine.setAttribute('stroke-width', 2);
        svg.appendChild(mainLine);

        // 💡 刻度线和年份标签绘制子函数 (支持不同间隔和长度)
        function drawTick(year, interval) {
            // Y 坐标始终基于 100 年间隔来计算
            const yPos = (year - minYearToDraw) / YEAR_INTERVAL_NORMAL * spacing;

            // 刻度线的长度：100年间隔长一点，10年间隔短一点
            const tickLength = (interval === YEAR_INTERVAL_NORMAL) ? 10 : 5;

            // 1. 绘制刻度线
            const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            tick.setAttribute('x1', axisX - tickLength);
            tick.setAttribute('y1', yPos);
            tick.setAttribute('x2', axisX + tickLength);
            tick.setAttribute('y2', yPos);
            tick.setAttribute('stroke', 'black');
            tick.setAttribute('stroke-width', 1);
            svg.appendChild(tick);

            // 2. 绘制年份标签

            // Condition 1: 100年刻度 (Major ticks)
            const isMajorTickLabel = (year % YEAR_INTERVAL_NORMAL === 0);

            // Condition 2: 1800年后的10年刻度，但不是100年的整数倍 (Minor labels)
            // 确保只在精细划分区域 (>= 1800) 绘制 10, 20, 30... 刻度标签
            const isMinorTickLabel = (year >= FINE_GRAIN_START_YEAR && year % YEAR_INTERVAL_FINE === 0 && year % YEAR_INTERVAL_NORMAL !== 0);

            if (isMajorTickLabel || isMinorTickLabel) {
                const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');

                // 将标签放置在刻度线左侧
                const labelXOffset = (tickLength + 5);

                label.setAttribute('x', axisX - labelXOffset);
                label.setAttribute('y', yPos + (fontSize / 3));
                label.setAttribute('text-anchor', 'end');
                label.setAttribute('font-size', fontSize);

                // ⭐ 关键修改：为 10年刻度设置绿色，100年刻度设置黑色
                if (isMinorTickLabel) {
                    label.setAttribute('fill', 'green');
                } else {
                    label.setAttribute('fill', 'black');
                }

                label.textContent = year >= 0 ? year + '年' : '前' + Math.abs(year) + '年';
                svg.appendChild(label);
            }
        }

        // --- 绘制间隔线和年份标签 ---

        // 1. 绘制 1800 年之前 (100 年间隔)
        // 从设定的起点开始，到精细划分的起点前一个 100 年刻度结束
        const normalEndYear = Math.floor((FINE_GRAIN_START_YEAR - 1) / YEAR_INTERVAL_NORMAL) * YEAR_INTERVAL_NORMAL;

        for (let year = minYearToDraw; year <= normalEndYear; year += YEAR_INTERVAL_NORMAL) {
            drawTick(year, YEAR_INTERVAL_NORMAL);
        }

        // 2. 绘制 1800 年及之后 (10 年间隔)
        for (let year = FINE_GRAIN_START_YEAR; year <= currentMaxYear; year += YEAR_INTERVAL_FINE) {
            drawTick(year, YEAR_INTERVAL_FINE);
        }


        // --- 绘制历史事件点和说明 ---
        let currentYOffset = 0; // 用于错开事件说明文字的垂直位置
        const X_OFFSET = 10;

        const sortedEvents = Object.keys(eventData).sort((a, b) => Number(a) - Number(b));

        sortedEvents.forEach(yearStr => {
            const year = Number(yearStr);
            const [description, color] = eventData[yearStr];

            // 确保事件在用户设定的范围内
            if (year > currentMaxYear || year < minYearToDraw) return;

            // 计算事件点在 SVG 中的 Y 坐标 (基于 100 年间隔)
            const yPos = (year - minYearToDraw) / YEAR_INTERVAL_NORMAL * spacing;

            // 错位逻辑：确保事件文字不重叠
            if (yPos < currentYOffset + fontSize + 5) {
                currentYOffset += fontSize + 5;
            } else {
                currentYOffset = yPos;
            }

            // 1. 绘制小黑圆点
            const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            dot.setAttribute('cx', axisX);
            dot.setAttribute('cy', yPos);
            dot.setAttribute('r', dotSize);
            // 圆点颜色跟随文字颜色
            dot.setAttribute('fill', color || 'black');

            svg.appendChild(dot);

            // 2. 绘制指向事件说明的箭头线
            const lineToText = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            lineToText.setAttribute('x1', axisX);
            lineToText.setAttribute('y1', yPos);
            lineToText.setAttribute('x2', axisX + X_OFFSET + 5);
            lineToText.setAttribute('y2', currentYOffset);
            lineToText.setAttribute('stroke', 'gray');
            lineToText.setAttribute('stroke-width', 1);
            svg.appendChild(lineToText);

            // 3. 绘制历史事件说明文字
            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', axisX + X_OFFSET * 2);
            text.setAttribute('y', currentYOffset + (fontSize / 3));
            text.setAttribute('font-size', fontSize);
            text.setAttribute('fill', color || 'black');
            const yearText = year >= 0 ? year + '年' : '前' + Math.abs(year) + '年';

            // 提取事件描述部分
            const eventDesc = description.includes(' / ') ? description.split(' / ')[1] : description;
            text.textContent = yearText + ' / ' + eventDesc;
            svg.appendChild(text);
        });
    }

    // ----------------------------------------------------------------
    // 4. 交互功能 (缩放、样式、范围) - 包含 localStorage 保存逻辑
    // ----------------------------------------------------------------

    // 缩放函数
    function handleZoom(factor) {
        currentZoom = Math.max(0.5, currentZoom * factor);
        currentZoom = Math.min(50.0, currentZoom);

        // 保存缩放级别
        localStorage.setItem('timelineZoom', currentZoom.toFixed(2));

        drawTimeline();
    }

    // 更新时间轴范围函数
    function handleUpdate() {
        let newMinYear = parseInt(minYearInput.value);
        let newMaxYear = parseInt(maxYearInput.value);

        // 确保最小年份是 100 的倍数，向下取整
        if (newMinYear % YEAR_INTERVAL_NORMAL !== 0) {
            newMinYear = Math.floor(newMinYear / YEAR_INTERVAL_NORMAL) * YEAR_INTERVAL_NORMAL;
            minYearInput.value = newMinYear;
        }

        // 确保最大年份是 100 的倍数，向上取整
        if (newMaxYear % YEAR_INTERVAL_NORMAL !== 0) {
            newMaxYear = Math.ceil(newMaxYear / YEAR_INTERVAL_NORMAL) * YEAR_INTERVAL_NORMAL;
            maxYearInput.value = newMaxYear;
        }

        // 简单校验：确保最大年份大于最小年份
        if (newMaxYear <= newMinYear) {
            alert("最大年份必须大于起始年份！");
            return;
        }

        currentMinYear = newMinYear;
        currentMaxYear = newMaxYear;

        // 保存最小和最大年份
        localStorage.setItem('timelineMinYear', currentMinYear);
        localStorage.setItem('timelineMaxYear', currentMaxYear);

        drawTimeline();
    }

    // 监听器
    zoomInBtn.addEventListener('click', () => handleZoom(1.2));
    zoomOutBtn.addEventListener('click', () => handleZoom(1 / 1.2));

    // 监听样式变化，并保存到 localStorage
    fontSizeInput.addEventListener('change', () => {
        localStorage.setItem('timelineFontSize', fontSizeInput.value);
        drawTimeline();
    });

    dotSizeInput.addEventListener('change', () => {
        localStorage.setItem('timelineDotSize', dotSizeInput.value);
        drawTimeline();
    });

    updateBtn.addEventListener('click', handleUpdate);

    // 初始加载数据和绘图
    loadData();
});