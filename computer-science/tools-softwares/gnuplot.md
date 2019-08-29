- mac下png得到的结果pixelated，最好使用pngcairo(效果也一般)，或先生成svg／postscript（使用跟字体匹配的分辨率），然后在转成图片(使用高分辨率)
- 数据集里如果有些点没有数据，可以设置为NaN，这样数据点不会绘制，但xaxis会被绘制
- 默认border是四边形的，如果只要左边和底边：`set border 3`
- label是指xy axis下面的描述性信息
- 因为字体的关系，如果在terminal设置高的size值，字体很小。因此可以在terminal内设置小的size，但在类型转换时使用高分辨率，来保证图片效果和质量
- 旋转xlabel：`set xtics rotate by 45 right nomirror`，注意一定要有right，否则label可能跟xaxis交叉

### svg 转成 png
- `brew install librsvg`
- `rsvg-convert -b white -w 3000 -h 2000 workout.svg -o output.png`
- `rsvg-convert`默认会添加背景色，需要显示设置

