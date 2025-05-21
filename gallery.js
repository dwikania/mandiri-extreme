const imageList = [
  'image1.jpg',
  'image2.jpg',
  'image3.jpg'
  // Tambahkan nama file sesuai yang kamu upload
];

const galleryContainer = document.querySelector('.gallery');

imageList.forEach(image => {
  const img = document.createElement('img');
  img.src = `images/${image}`;
  img.alt = image;
  galleryContainer.appendChild(img);
});
