document.addEventListener('mousemove', function(e) {
    // Create a new DNA trail element
    const trail = document.createElement('div');
    trail.classList.add('dna-trail');
    
    // Position the trail element at the mouse coordinates
    trail.style.left = `${e.pageX - 10}px`; // Subtract to center the icon at the cursor
    trail.style.top = `${e.pageY - 10}px`;  // Subtract to center the icon at the cursor
    
    // Append the trail element to the #trail container
    document.getElementById('trail').appendChild(trail);
    
    // Remove the trail element after animation duration (1s)
    setTimeout(function() {
        trail.remove();
    }, 1000); // Time should match the fadeOut animation duration
});
