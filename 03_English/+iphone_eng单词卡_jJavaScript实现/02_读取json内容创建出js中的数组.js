const
fs = require('fs');
const
path = require('path');


// 定义JSON文件路径
const
jsonPath = path.join('C:', 'phpStorm_proj', '02_myself_ID_EGO', '03_English', '+iphone_eng单词卡_jJavaScript实现',
                     'allword.json');


//这个空数组, 就使用来接收json中的内容的
var arr_allword=[];


// 读取JSON文件
fs.readFile(jsonPath, 'utf8', (err, data) => {
if (err)
{
    console.error('读取文件时出错:', err);
return;
}

try {
// 解析JSON数据为JavaScript数组
arr_allword = JSON.parse(data);

// 验证数据格式
if (!Array.isArray(arr_allword)) {
throw new Error('JSON数据不是数组格式');
}

// 打印数组长度和第一条数据作为验证
console.log(`成功读取 ${arr_allword.length} 条单词数据`);
console.log('第一条数据:', arr_allword[0]);


//遍历打印出数组中的所有元素
for (i in arr_allword)
{
    console.log(arr_allword[i])
}

// 在此处可以使用arr_allword数组进行后续操作
// 例如：处理数据、显示内容等

} catch (parseError) {
console.error('解析JSON时出错:', parseError);
}
});

