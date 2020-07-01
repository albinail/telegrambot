# telegrambot
1. Вариант "all model": использована предобученная модель vgg19 из лекции, функционал перенесен  в отдельный класс. Модель стандартная, работает на всех изображениях хорошо, но очень тяжелая в первоначальном виде.

1.1.Оригинальное изображение, в стиле Звездной ночи Ван Гога, в стиле импрессионистов.
<div align="left">
<img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/cat.JPG" width="200" float= "left"  > <img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/vgg_cat_van.png" width="200" float= "left" ><img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/vgg_impr_cat.png" width="200" float= "left" >

</div>

1.2.  Модель хорошо переносит абстрактные стили, например Кандинского
<div align="left">
<img src="https://avatars.mds.yandex.net/get-pdb/902733/b754c609-3527-415c-a115-9f1a2665035a/s1200?webp=false" width="200" float= "left"  ><img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/vgg_all_cat_kand.png" width="200" float= "left"  ><img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg" width="200" float= "left"  ><img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/vgg_all_cat_kand1913.png" width="200" float= "left"  >
  
</div>

2. Вариант "alexnet". Мне было интересно попробовать другую модель, кроме стандартной vgg, желательно более легкую. Результаты мне понравились: они отличаются от vgg19. Отлично переносятся стили классической живописи, импрессионистов и экспрессионистов (мне даже больше нравятся чем от vgg  и расчет гораздо быстрее). Но на совершенно абстрактных, вроде картины Кандинского "Композиция 7" модель может работать хуже. Можно именно под такие произведения подстроить коэффициенты, но тогда будет хуже обрабатываться остальное.

2.1. Оригинальное изображение, в стиле Звездной ночи Ван Гога, в стиле импрессионистов. Есть отличие от vgg, поверхностный стиль передан лучше, имитация картин также лучше.

<div align="left">

<img src="https://github.com/albinail/telegrambot/blob/master/all%20model/output/cat.JPG" width="200" float= "left"  > <img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/cat_van.png" width="200" float= "left" ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/impr_cat.jpg" width="200" float= "left" >
</div>

2.2. Модель хуже переносит абстрактные стили, самый плохой пример - Композиция 7 Кандинского
<div align="left">
<img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/kand.jpg" width="200" float= "left"  ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/kand_cat.jpg" width="200" float= "left"  >

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg" width="200" float= "left"  ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/Kand7_wood.jpg" width="200" float= "left"  ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/Kand7_cat.jpg" width="200" float= "left"  >
</div>

2.3. Модель хорошо переносит стиль письма и материалы: может сделать из масла -пастель

<div align="left">

<img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/nalb.png" width="200" float= "left"  > <img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/dega_ist.png" width="200" float= "left" ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/nalb_dega.png" width="200" float= "left" >
</div>

<div align="left">

<img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/Expressionism-Hubert-Roestenburg-Alpenzicht-Buching-Halblech-L.jpg" width="200" float= "left"  > <img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/Expressionism_wood.jpg" width="200" float= "left" ><img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/dali.png" width="200" float= "left" >
<img src="https://github.com/albinail/telegrambot/blob/master/alexnet/examples/dali_style.png" width="200" float= "left" >
</div>
