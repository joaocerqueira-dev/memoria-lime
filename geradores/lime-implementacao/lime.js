/* Var Chocolates · JS personalizado (aba Código → JavaScript)
   Revela as seções da Home ao entrarem na tela. */
document.addEventListener("DOMContentLoaded", function () {
  var alvos = document.querySelectorAll(".productList, .bannerModule, .review, .newsletter, .html");
  if (!("IntersectionObserver" in window)) return;
  var obs = new IntersectionObserver(function (itens) {
    itens.forEach(function (i) {
      if (i.isIntersecting) { i.target.classList.add("is-visible"); obs.unobserve(i.target); }
    });
  }, { threshold: 0.15 });
  alvos.forEach(function (el, k) { if (k > 0) { el.classList.add("var-reveal"); obs.observe(el); } });
});
