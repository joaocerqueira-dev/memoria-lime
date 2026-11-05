// Preenche o formulário de produto da Irroba (todas as abas carregadas) com um item de produtos-bo.json.
window.fillBo = function (p) {
  const f = document.querySelector('#form-product');
  const set = (n, v) => {
    const e = f.querySelector(`[name="${n}"]`);
    if (!e) return n + '? ';
    e.value = v;
    e.dispatchEvent(new Event('input', { bubbles: true }));
    e.dispatchEvent(new Event('change', { bubbles: true }));
    return '';
  };
  const editor = (n, html) => {
    const ta = f.querySelector(`[name="${n}"]`);
    if (!ta) return n + '? ';
    ta.value = html;
    const w = ta.nextElementSibling && ta.nextElementSibling.querySelector('.se-wrapper-wysiwyg, [contenteditable=true]');
    if (w) { w.innerHTML = html; w.dispatchEvent(new Event('input', { bubbles: true })); }
    return '';
  };
  let miss = '';
  miss += set('product_description[2][name]', p.nome);
  miss += set('product_description[3][name]', p.nome);
  miss += set('keyword', p.url);
  miss += set('sku', p.sku);
  miss += set('model', p.sku);
  miss += set('price', p.preco);
  miss += set('weight', p.peso);
  miss += set('length', p.dims[0]);
  miss += set('width', p.dims[1]);
  miss += set('height', p.dims[2]);
  miss += set('product_description[2][meta_title]', p.nome + ' | Bô Eugenia Bologna');
  miss += set('product_description[2][meta_description]', p.resumo.slice(0, 155));
  editor('product_description[2][description_resume]', p.pano ? '<p>' + p.resumo + '</p>' : '');
  miss += editor('product_description[2][description]', p.desc);
  const sc = f.querySelector('[name="product_category[]"]');
  [...sc.options].forEach(o => (o.selected = p.cats.includes(Number(o.value))));
  if (window.jQuery) jQuery(sc).trigger('change');
  const sl = f.querySelector('[name="product_list[]"]');
  if (sl) { [...sl.options].forEach(o => (o.selected = false)); if (window.jQuery) jQuery(sl).trigger('change'); }
  f.querySelector('[name="product_image[0][image]"]').value = p.imgs[0];
  [...f.querySelectorAll('[name^="product_image["]')].filter(e => !/^product_image\[0\]/.test(e.name)).forEach(e => (e.disabled = true));
  f.querySelectorAll('.bo-extra-img').forEach(e => e.remove());
  p.imgs.slice(1).forEach((src, k) => {
    const n = k + 1;
    [['image', src], ['sort_order', String(n)]].forEach(([fld, v]) => {
      const h = document.createElement('input');
      h.type = 'hidden'; h.className = 'bo-extra-img'; h.name = `product_image[${n}][${fld}]`; h.value = v;
      f.appendChild(h);
    });
  });
  const st = f.querySelector('[name="status"]');
  if (st && st.type === 'checkbox') st.checked = true;
  return miss || 'ok';
};
