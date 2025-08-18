document.addEventListener("DOMContentLoaded", () => {
  const menu = document.getElementById("mobileMenu");
  const hamburger = document.querySelector(".hamburger");
  const closeBtn = document.getElementById("closeMenu");
  const menuLinks = menu?.querySelectorAll("a");

  const toggleMenu = () => {
    menu?.classList.toggle("active");
    hamburger?.classList.toggle("active");
    document.body.style.overflow = menu?.classList.contains("active") ? "hidden" : "auto";
  };

  const closeMenu = () => {
    menu?.classList.remove("active");
    hamburger?.classList.remove("active");
    document.body.style.overflow = "auto";
  };

  hamburger?.addEventListener("click", toggleMenu);
  closeBtn?.addEventListener("click", closeMenu);
  menuLinks?.forEach(link => link.addEventListener("click", closeMenu));
});
