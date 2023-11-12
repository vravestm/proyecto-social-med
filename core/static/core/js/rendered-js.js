let img = document.getElementById("img_perfil");
let input = document.getElementById("input_img");

input.onchange = (e) => {
    if (input.files[0]) img.src = URL.createObjectURL(input.files[0]);
};
