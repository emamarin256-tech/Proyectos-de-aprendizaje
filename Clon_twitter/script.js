// #region variables

const pagina_principal = document.querySelector(".pagina-principal");
const pag_inicio_sesion = document.querySelector(".pag-inicio-sesion");
const Cont_medio = document.querySelector(".contenido-enmedio");
const boton_arriba = document.querySelector(".boton-arriba");
const pag_noti = document.querySelector(".pagina-noticias");
const cartel = document.querySelector(".cartel-inicio-sesion");
const x = document.querySelector("#cerrar");
const boton_postear = document.querySelector(".post-btn");
const fondo_nuev_post = document.querySelector(".nuevpost-contenedor");
const nuev_post = document.querySelector(".nuevpost");
const x_nuevpost = document.querySelector(".nuevpost-cabecera i");
const boton_inicio_session_principal = document.querySelector(".inicio-sesion-form-boton");
const boton_poster_nuevpost = document.querySelector(".nuevpost-cabecera button");
const boton_mas = document.querySelector(".nuevpost-iconos span");
const input_nuevpost = document.querySelector(".nuevpost-input");
const cartel_descartar = document.querySelector(".cartel-descartar");
const x_descartar = document.querySelector(".cartel-descartar #cerrar");

/* ******************************************** */
/* ******************************************** */
// #endregion

// #region Pagina principal
const ir_a_inicio_sesion = () => {
  pagina_principal.style.display = "none";
  pag_inicio_sesion.style.display = "grid";
};
Cont_medio.addEventListener("click", (e) => {
  if (e.target.classList[1] === "boton-pagina-principal") ir_a_inicio_sesion();
});

// configuracion boton inicio sesion arriba
boton_arriba.addEventListener("click", () => {
  const inputUI = document.querySelector(".usuario-info");
  const inputP = document.querySelector(".password");

  if (inputUI.value !== "" && inputP.value !== "") {
    pagina_principal.style.display = "none";
    pag_noti.style.display = "block";
  } else {
    cartel.style.display = "block";
    ir_a_inicio_sesion();
  }
});
// #endregion

// #region pag inicio sesion
// #region ir a pag noticias

const ir_a_pag_noticias = () => {
  pag_inicio_sesion.style.display = "none";
  pag_noti.style.display = "block";
};

boton_inicio_session_principal.addEventListener("click", () => {
  const inputUI = document.querySelector(".usu-info");
  const inputP = document.querySelector(".paswrd");

  if (inputUI.value !== "" && inputP.value !== "") {
    ir_a_pag_noticias();
  } else {
    inputP.style.borderColor = "red";
    inputUI.style.borderColor = "red";
    cartel.style.display = "block";
  }
});
//#endregion
// #region cerrar cartel
x.addEventListener("click", (e) => {
  const inputUI = document.querySelector(".usu-info");
  const inputP = document.querySelector(".paswrd");
  cartel.style.display = "none";
  inputP.style.borderColor = "#ddd";
  inputUI.style.borderColor = "#ddd";
});
//#endregion
//#endregion

// #region pag noticias
// #region mostrar nuevpost
boton_postear.addEventListener("click", (e) => {
  fondo_nuev_post.style.visibility = "visible";
  fondo_nuev_post.style.opacity = 1;
  nuev_post.style.display = "block";

});
// #endregion
//#region cerrar newpost
x_nuevpost.addEventListener("click", (e) => {
  if (input_nuevpost.value.length > 0) {
    cartel_descartar.style.display = "grid";
  } else {
    fondo_nuev_post.style.visibility = "hidden";
    fondo_nuev_post.style.opacity = 0;
    nuev_post.style.display = "none";
  }
});
// #endregion
//#region opacidad + y post

function cambiar_opacidad(x) {
  boton_mas.style.opacity = x;
  boton_poster_nuevpost.style.opacity = x;
}

input_nuevpost.addEventListener("input", () => {
  if (input_nuevpost.value.length > 0) {
    cambiar_opacidad(1);
  } else {
    cambiar_opacidad(0.5);
  }
});
//#endregion
//#region cerrar_artel_descartar
x_descartar.addEventListener("click", (e) => {
  cartel_descartar.style.display = "none";
});
//#endregion
// #region eleccion cartel_decartar
const boton_guardar = document.querySelector(".guardar");
const boton_descartar = document.querySelector(".descartar");
boton_descartar.addEventListener("click", (e) => {
  input_nuevpost.value = "";
  cartel_descartar.style.display = "none";
  fondo_nuev_post.style.visibility = "hidden";
  fondo_nuev_post.style.opacity = 0;
  nuev_post.style.display = "none";
});
boton_guardar.addEventListener("click", (e) => {
  cartel_descartar.style.display = "none";
  fondo_nuev_post.style.visibility = "hidden";
  fondo_nuev_post.style.opacity = 0;
  nuev_post.style.display = "none";
});
//#endregion
//#region info del usuario
//#region mostrar_info_usuario
const barra_info_usu = document.querySelector(".barra-lateral-contenedor");
const boton_usuario = document.querySelector(".usuario");
boton_usuario.addEventListener("click", (e) => {
  barra_info_usu.style.right = 0;
  barra_info_usu.style.visibility = "visible";
  barra_info_usu.style.opacity = 1;
});
//#endregion
//#region cerrar_info
const x_info_usuario = document.querySelector(".barra-lateral-cabecera i");
x_info_usuario.addEventListener("click", () => {
  barra_info_usu.style.right = -30;
  barra_info_usu.style.visibility = "hidden";
  barra_info_usu.style.opacity = 0;
});
//#endregion

//#endregion
//#region modo oscuro
const boton_modo_oscuro = document.querySelector(".opcion");
const circulo_modo_oscuro = document.querySelector(".circulo");
const oscuros1 = document.querySelectorAll(".elementos_de_oscuro1");
const oscuros2 = document.querySelectorAll(".elementos_de_oscuro2");
const claro_si = document.querySelectorAll(".claro-que-si")

boton_modo_oscuro.addEventListener("click", () => {
    circulo_modo_oscuro.classList.toggle("move");
    Array.from(oscuros1).map((oscu1) => 
    oscu1.classList.toggle("oscuro-1"));
    Array.from(oscuros2).map((oscu2) => 
    oscu2.classList.toggle("oscuro-2"));
    Array.from(claro_si).map((claro0) => 
    claro0.classList.toggle("claro"));
});

//#endregion
//#endregion
