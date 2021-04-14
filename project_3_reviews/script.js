let index = 0;
let names = ["Lorem ipsum", "Sed dignissim", "Class", "Sed lectus", "Curabitur sit amet"];
let reviews = [
    "Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. ",
    "Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. ",
    "Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit.",
    "Integer euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue elementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit vel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. ",
    "Nulla facilisi. Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. Vestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede."
];
let nme = document.getElementById("name");
let review = document.getElementById("quote");
nme.textContent = names[0];
review.textContent = reviews[0]

let next = document.getElementById("next");
let prev = document.getElementById("prev");
let rand = document.getElementById("rand");


next.addEventListener("click",function(){index++;if(index>4)index=0;update(index);});
prev.addEventListener("click",function(){index--;if(index<0)index=4;update(index);});
rand.addEventListener("click", function(){index=Math.random()*5; index=Math.floor(index); update(index);})

function update(index){
    nme.textContent = names[index];
    review.textContent = reviews[index];
}