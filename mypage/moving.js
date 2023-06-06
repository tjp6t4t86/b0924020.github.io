<script>
setInterval(play,3000);
var index=0;

function play(){
  
  var imgs = document.getElementById("pictures").
               getElementsByTagName("img");
  var bigImg = document.getElementById("big");
  imgs[index].classList.remove("selected");
  index++;
  if(index == imgs.length) index=0;
  imgs[index].classList.add("selected");
  bigImg.setAttribute("src",imgs[index].getAttribute("src"));
}
</script>