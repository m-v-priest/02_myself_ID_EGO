// 示例数据
// 使用从 data_WordIELTS.js 导入的 data_WordIELTS
const arr_allword = wordData;

const bgImages = data_bgImages;


// 获取DOM元素
const idContent = document.getElementById('idContent');
const wordContent = document.getElementById('wordContent');
const definitionContent = document.getElementById('definitionContent');
const etymologyContent = document.getElementById('etymologyContent');
const wordHeader = document.getElementById('wordHeader');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const randomBtn = document.getElementById('randomBtn');
const progress = document.getElementById('progress');
const bgOverlay = document.getElementById('bgOverlay');
const opacitySlider = document.getElementById('opacitySlider');
const opacityValue = document.getElementById('opacityValue');

// 获取新DOM元素
const scaleSlider = document.getElementById('scaleSlider');
const scaleValue = document.getElementById('scaleValue');
const fitHeightBtn = document.getElementById('fitHeightBtn');
const fitWidthBtn = document.getElementById('fitWidthBtn');


// 新增：更新背景缩放比例
function updateBackgroundScale(value) {
    const scale = 1 + (value - 100) / 100;
    document.body.style.setProperty('--bg-scale', scale);
    scaleValue.textContent = `${value}%`;
    // 当使用缩放滑块时，将 background-size 恢复为 cover
    document.body.style.setProperty('--bg-size', 'contain');
}

// 新增：更新背景尺寸
function updateBackgroundSize(sizeType) {
    // 重置缩放滑块
    scaleSlider.value = 100;
    scaleValue.textContent = '100%';
    document.body.style.setProperty('--bg-scale', '1');

    if (sizeType === 'height') {
        document.body.style.setProperty('--bg-size', 'auto 100%');
    } else if (sizeType === 'width') {
        document.body.style.setProperty('--bg-size', '100% auto');
    }
}


// 底部按钮
const prevBtnBottom = document.getElementById('prevBtnBottom');
const nextBtnBottom = document.getElementById('nextBtnBottom');
const randomBtnBottom = document.getElementById('randomBtnBottom');


// 当前单词索引
let currentIndex = 0;

// 设置背景图
function setBackgroundImage(imagePath) {
    const img = new Image();
    img.onload = function() {
        // 设置CSS变量
        document.body.style.setProperty('--bg-image', `url('${imagePath}')`);
        // 默认设置为适配高度
        updateBackgroundSize('height');
    };
    img.onerror = function() {
        // 使用默认渐变背景
        document.body.style.setProperty('--bg-image', "linear-gradient(135deg, rgba(110, 142, 251, 0.7), rgba(167, 119, 227, 0.7))");
        document.body.style.setProperty('--bg-size', 'cover');
    };
    img.src = imagePath;
}

// 设置随机背景图
function setRandomBackground() {
    // 确保 bgImages 是一个数组且不为空
    if (Array.isArray(bgImages) && bgImages.length > 0) {
        const randomIndex = Math.floor(Math.random() * bgImages.length);
        const randomImage = bgImages[randomIndex];
        // 设置CSS变量
        document.body.style.setProperty('--bg-image', `url('${randomImage}')`);
    }
}

// 更新背景层透明度
function updateBackgroundOpacity(value) {
    const opacity = value / 100;
    bgOverlay.style.opacity = 1 - opacity;
    opacityValue.textContent = `${value}%`;
}

// 显示当前单词
function displayCurrentWord() {
    const word = arr_allword[currentIndex];

    idContent.textContent = word.id;
    wordContent.textContent = word.词头;
    definitionContent.innerHTML = word.释义和例句;
    etymologyContent.textContent = word.词根词缀;
    wordHeader.textContent = word.词头;

    // 更新进度
    progress.textContent = `${currentIndex + 1} / ${arr_allword.length}`;
}

// 按钮点击处理函数
function handleButtonClick(action) {
    // 更新单词索引
    if (action === 'prev') {
        currentIndex = currentIndex > 0 ? currentIndex - 1 : arr_allword.length - 1;
    } else if (action === 'next') {
        currentIndex = currentIndex < arr_allword.length - 1 ? currentIndex + 1 : 0;
    } else if (action === 'random') {
        let newIndex;
        do {
            newIndex = Math.floor(Math.random() * arr_allword.length);
        } while (newIndex === currentIndex && arr_allword.length > 1);
        currentIndex = newIndex;
    }

    // 更新单词显示
    displayCurrentWord();

    // 更新背景图
    setRandomBackground();
}

// 顶部按钮事件
prevBtn.addEventListener('click', () => handleButtonClick('prev'));
nextBtn.addEventListener('click', () => handleButtonClick('next'));
randomBtn.addEventListener('click', () => handleButtonClick('random'));

// 底部按钮事件
prevBtnBottom.addEventListener('click', () => handleButtonClick('prev'));
nextBtnBottom.addEventListener('click', () => handleButtonClick('next'));
randomBtnBottom.addEventListener('click', () => handleButtonClick('random'));

// 透明度滑块事件
opacitySlider.addEventListener('input', function() {
    updateBackgroundOpacity(this.value);
});

// 新增：缩放滑块事件
scaleSlider.addEventListener('input', function() {
    updateBackgroundScale(this.value);
});

// 新增：尺寸按钮事件
fitHeightBtn.addEventListener('click', () => updateBackgroundSize('height'));
fitWidthBtn.addEventListener('click', () => updateBackgroundSize('width'));


// 添加键盘快捷键支持
document.addEventListener('keydown', (e) => {
    switch(e.key) {
        case 'ArrowLeft':
            handleButtonClick('prev');
            break;
        case 'ArrowRight':
            handleButtonClick('next');
            break;
        case ' ':
        case 'r':
            handleButtonClick('random');
            break;
    }
});

// 初始化显示
displayCurrentWord();
setRandomBackground(); // 确保这个函数在页面加载时被调用
updateBackgroundOpacity(50);
updateBackgroundScale(100);


// iOS Safari 特殊处理
if (navigator.userAgent.match(/(iPad|iPhone|iPod)/i)) {
    // 添加iOS专用的事件监听器
    window.addEventListener('orientationchange', function() {
        // 重新加载背景图以解决iOS缩放问题
        const currentBg = document.body.style.getPropertyValue('--bg-image');
        if (currentBg && currentBg !== 'none') {
            const imgPath = currentBg.replace(/url\("|"\)/g, '');
            setBackgroundImage(imgPath);
        }
    });
}