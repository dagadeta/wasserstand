function main() {
    let waterdiv1 = document.getElementById("waterdiv1");
    let waterdiv2 = document.getElementById("waterdiv2");
    let waterdiv3 = document.getElementById("waterdiv3");
    let waterdiv4 = document.getElementById("waterdiv4");
    let waterdiv5 = document.getElementById("waterdiv5");

    let water1 = true;
    let water2 = true;
    let water3 = true;
    let water4 = false;
    let water5 = false;

    if (water1 === true) {
        waterdiv1.style.backgroundColor = "royalblue";
    } else {
        waterdiv1.style.backgroundColor = "lightslategrey";
    }
    if (water2 === true) {
        waterdiv2.style.backgroundColor = "royalblue";
    } else {
        waterdiv2.style.backgroundColor = "lightslategrey";
    }
    if (water3 === true) {
        waterdiv3.style.backgroundColor = "royalblue";
    } else {
        waterdiv3.style.backgroundColor = "lightslategrey";
    }
    if (water4 === true) {
        waterdiv4.style.backgroundColor = "royalblue";
    } else {
        waterdiv4.style.backgroundColor = "lightslategrey";
    }
    if (water5 === true) {
        waterdiv5.style.backgroundColor = "royalblue";
    } else {
        waterdiv5.style.backgroundColor = "lightslategrey";
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    main()
})