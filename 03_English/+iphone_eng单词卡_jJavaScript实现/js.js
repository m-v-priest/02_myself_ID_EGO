
// 背景图片列表 - 替换为您的实际图片路径
// const bgImages = [
//     "bg_img/t_background_image-01.png",
//     "bg_img/t_background_image-02.png",
// ];

const bgImages = [
    "bg_img/bg003.png",
    "bg_img/bg004.png",
    "bg_img/bg005.png",
    "bg_img/bg006.png",
    "bg_img/bg007.png",
    "bg_img/bg008.png",
    "bg_img/bg009.avif",
    "bg_img/bg009.jpg",
    "bg_img/bg010.avif",
    "bg_img/bg011.jpg",
    "bg_img/bg012.webp",
    "bg_img/bg013.webp",
    "bg_img/bg014.jpg",
    "bg_img/bg015.jpg",
    "bg_img/bg016.webp",
    "bg_img/bg017.jpg",
    "bg_img/bg018.jpg",
    "bg_img/bg019.webp",
    "bg_img/bg020.jpg",
    "bg_img/bg021.jpg",
    "bg_img/bg022.png",
    "bg_img/bg023.jpg",
    "bg_img/bg024.jpg",
    "bg_img/bg025.png",
    "bg_img/bg026.jpg",
    "bg_img/bg027.svg",
    "bg_img/bg028.webp",
    "bg_img/bg029.jpg",
    "bg_img/bg030.jpg",
    "bg_img/bg031.jpg",
    "bg_img/bg032.png",
    "bg_img/bg033.jpg",
    "bg_img/bg034.jpg",
    "bg_img/bg035.jpg",
    "bg_img/bg036.webp",
    "bg_img/bg037.jpg",
    "bg_img/bg038.jpg",
    "bg_img/bg039.jpg",
    "bg_img/bg040.gif",
    "bg_img/bg041.png",
    "bg_img/bg042.jpg",
    "bg_img/bg043.jpg",
    "bg_img/g001.png",
    "bg_img/g002.png"
];

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
const bgInfo = document.getElementById('bgInfo');

// 示例数据
const arr_allword = [
    {
        id: '1',
        '词头': 'apple',
        '释义和例句': 'n. 苹果\n例: I eat an apple every day.\n例: The apple tree is full of fruits.',
        '词根词缀': '来自古英语 æppel, 水果的总称'
    },
    {
        id: '2',
        '词头': 'book',
        '释义和例句': 'n. 书籍\nv. 预订\n例: This is an interesting book.\n例: I booked a table for two at the restaurant.',
        '词根词缀': '来自古英语 bōc, 与 beech(山毛榉)有关，因早期文字刻在山毛榉木板上'
    },
    {
        id: '3',
        '词头': 'computer',
        '释义和例句': 'n. 计算机\n例: My computer is running slowly today.\n例: She works as a computer programmer.',
        '词根词缀': 'compute(计算) + -er(表示工具)'
    },
    {
        id: '4',
        '词头': 'democracy',
        '释义和例句': 'n. 民主\n例: Democracy is a system of government by the whole population.\n例: The country transitioned to democracy in the 1990s.',
        '词根词缀': 'demo(人民) + cracy(统治) → 人民统治'
    },
    {
        id: '5',
        '词头': 'ephemeral',
        '释义和例句': 'adj. 短暂的\n例: Fame in the internet age is often ephemeral.\n例: The beauty of cherry blossoms is ephemeral.',
        '词根词缀': 'epi(在...之上) + hemera(天) → 只持续一天的'
    },
    {
        id: '6',
        '词头': 'facetious',
        '释义和例句': 'adj. 开玩笑的，轻浮的\n例: He was being facetious when he said he could fly.\n例: Her facetious remarks annoyed the teacher.',
        '词根词缀': '来自拉丁语 facetia(玩笑)'
    },
    {
        id: '7',
        '词头': 'gregarious',
        '释义和例句': 'adj. 爱社交的，群居的\n例: She is very gregarious and loves parties.\n例: Sheep are gregarious animals.',
        '词根词缀': 'greg(群体) + -arious(有...性质的)'
    },
    {
        id: '8',
        '词头': 'harbinger',
        '释义和例句': 'n. 预兆，先驱\nv. 预告\n例: The robin is a harbinger of spring.\n例: These events may harbinger major changes.',
        '词根词缀': '来自古法语 herbergier(提供住宿)，原指先行安排住宿的人'
    }
];

// 当前单词索引
let currentIndex = 0;




// 设置背景图的新函数
function setBackgroundImage(imagePath) {
    const img = new Image();
    img.onload = function() {
        // 获取图片原始尺寸
        const imgWidth = this.width;
        const imgHeight = this.height;

        // 获取视窗尺寸
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;

        // 判断图片方向
        const isPortrait = imgHeight > imgWidth;

        // 设置背景图样式
        document.body.style.backgroundImage = `url('${imagePath}')`;

        if (isPortrait) {
            // 竖图：高度适配视窗高度
            document.body.style.backgroundSize = `auto ${windowHeight}px`;
        } else {
            // 横图：宽度适配视窗宽度
            document.body.style.backgroundSize = `${windowWidth}px auto`;
        }

        bgInfo.textContent = `背景图: ${imagePath.split('/').pop()}`;
    };
    img.onerror = function() {
        document.body.style.backgroundImage = "linear-gradient(135deg, rgba(110, 142, 251, 0.7), rgba(167, 119, 227, 0.7))";
        bgInfo.textContent = "背景图: 默认渐变";
    };
    img.src = imagePath;
}


// 设置随机背景图
// function setRandomBackground() {
//     if (bgImages.length === 0) return;
//
//     const randomIndex = Math.floor(Math.random() * bgImages.length);
//     const imagePath = bgImages[randomIndex];
//
//     // 创建新的Image对象来检查图片是否存在
//     const img = new Image();
//     img.onload = function() {
//         document.body.style.backgroundImage = `url('${imagePath}')`;
//         bgInfo.textContent = `背景图: ${imagePath.split('/').pop()}`;
//     };
//     img.onerror = function() {
//         // 如果图片加载失败，使用默认背景
//         document.body.style.backgroundImage = "linear-gradient(135deg, rgba(110, 142, 251, 0.7), rgba(167, 119, 227, 0.7))";
//         bgInfo.textContent = "背景图: 默认渐变";
//     };
//     img.src = imagePath;
// }

// 替换原有的setRandomBackground函数
function setRandomBackground() {
    if (bgImages.length === 0) return;
    const randomIndex = Math.floor(Math.random() * bgImages.length);
    setBackgroundImage(bgImages[randomIndex]);
}



// 更新背景层(背景图片)透明度
function updateBackgroundOpacity(value) {
    // 将滑块值转换为透明度值 (0-1)
    const opacity = value / 100;  //如果是50/100,即50%的透明度.
    /*
    value：一个0到100之间的数值，表示用户通过滑块设置的背景透明度百分比值。
    const opacity = value / 100;：将传入的百分比值（0-100）转换为0到1之间的透明度值（0表示完全透明，1表示完全不透明）。例如，如果滑块值为50，则opacity为0.5。
     */


    // 更新背景覆盖层的透明度
    bgOverlay.style.opacity = 1 - opacity;
    /*
    bgOverlay.style.opacity = 1 - opacity;：这里使用了一个背景覆盖层（一个半透明的遮罩层）来控制背景图的可见度。注意，我们设置的是覆盖层的透明度，而不是背景图片本身的透明度。
        当滑块值为0（完全透明）时，覆盖层的透明度为1（完全不透明），此时覆盖层会完全遮挡背景图，用户看不到背景图。
        当滑块值为100（完全不透明）时，覆盖层的透明度为0（完全透明），此时背景图完全可见。
        这种设计是为了通过调整覆盖层的透明度, 来间接控制背景图的可见度。
     */

    // 更新显示值
    opacityValue.textContent = `${value}%`;
    /*
    opacityValue.textContent =${value}%;：更新显示当前透明度百分比的文本元素，让用户知道当前的设置值。例如，如果滑块在50的位置，这里会显示“50%”。
    */
}



// 显示当前单词
function displayCurrentWord() {
    const word = arr_allword[currentIndex];

    idContent.textContent = word.id;
    wordContent.textContent = word.词头;
    definitionContent.textContent = word.释义和例句;
    etymologyContent.textContent = word.词根词缀;
    wordHeader.textContent = word.词头;

    // 更新进度
    progress.textContent = `${currentIndex + 1} / ${arr_allword.length}`;
}

// 按钮点击处理函数（包含背景图更新）
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

// 上一页按钮事件
prevBtn.addEventListener('click', () => handleButtonClick('prev'));

// 下一页按钮事件
nextBtn.addEventListener('click', () => handleButtonClick('next'));

// 随机单词按钮事件
randomBtn.addEventListener('click', () => handleButtonClick('random'));


// 透明度滑块事件
opacitySlider.addEventListener('input', function() {
    updateBackgroundOpacity(this.value);
});


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




// 窗口大小变化时重新调整背景图
window.addEventListener('resize', function() {
    // 重新应用背景图设置以确保自适应
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center';
    document.body.style.backgroundRepeat = 'no-repeat';

    const currentBg = document.body.style.backgroundImage;
    if (currentBg && currentBg !== 'none') {
        const imgPath = currentBg.replace(/url\("|"\)/g, '');
        setBackgroundImage(imgPath);
    }
});

// 初始化显示
displayCurrentWord();
setRandomBackground();