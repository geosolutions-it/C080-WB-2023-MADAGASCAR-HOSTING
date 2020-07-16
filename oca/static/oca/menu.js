function openNav() {
    document.getElementById("sideNavigation").style.width = "250px";
    document.getElementById("map").style.marginLeft = "250px";
    alert('ee');
    document.getElementById("fixer").style.position = "fixed";
}
 
function closeNav() {
    document.getElementById("sideNavigation").style.width = "0";
    document.getElementById("map").style.marginLeft = "0";    
    document.getElementById("fixer").style.position = "relative";
}
