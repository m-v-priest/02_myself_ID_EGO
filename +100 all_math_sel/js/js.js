
window.onload = function () {
    let myimgsize = 0
    let allimg = document.querySelectorAll("img");

    for (i in allimg) {
        myimgsize= allimg[i].naturalWidth; //获取所有图片的原始宽度尺寸
        allimg[i].width=myimgsize*0.3 //将图片宽度,重新设置为原式尺寸的0.3倍
    }

    //




}