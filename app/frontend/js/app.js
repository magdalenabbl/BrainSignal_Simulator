// Wait until the HTML page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Initialize the application
    initializeApp();

});


// Initialize common application logic
function initializeApp() {

    // Set the current page in the navigation
    setActiveNavigation();

    // Initialize navigation
    initializeNavigation();

}


// Highlight the current page in the navigation
function setActiveNavigation() {

    // Get the current URL path
    const currentPath = window.location.pathname;


    // Find all navigation links
    const links = document.querySelectorAll(
        ".sidebar a"
    );


    // Check every navigation link
    links.forEach(link => {

        // Get the link destination
        const href = link.getAttribute("href");


        // Skip links without href
        if (!href) {
            return;
        }


        // Remove the active class first
        link.classList.remove("active");


        // Check if this is the current page
        if (
            currentPath === href ||
            (
                currentPath === "/" &&
                href === "/"
            )
        ) {

            link.classList.add("active");

        }

    });

}


// Initialize navigation buttons
function initializeNavigation() {

    // Find all navigation links
    const links = document.querySelectorAll(
        ".sidebar a"
    );


    // Add a click handler to every link
    links.forEach(link => {

        link.addEventListener(
            "click",
            function () {

                // Remove active state from all links
                links.forEach(item => {
                    item.classList.remove("active");
                });


                // Mark the clicked link as active
                this.classList.add("active");

            }
        );

    });

}


// Show a message inside an element
function showMessage(
    elementId,
    message
) {

    // Find the element
    const element =
        document.getElementById(elementId);


    // Stop if the element does not exist
    if (!element) {
        return;
    }


    // Display the message
    element.textContent = message;

}


// Clear a message
function clearMessage(elementId) {

    // Find the element
    const element =
        document.getElementById(elementId);


    // Stop if the element does not exist
    if (!element) {
        return;
    }


    // Clear the content
    element.textContent = "";

}