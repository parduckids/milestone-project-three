$(document).ready(function () {
    // use cloudinary to generate image urls
    var myWidget = cloudinary.createUploadWidget({
      cloudName: 'dpcst40m2',
      // client-side uploads using a secure, unsigned preset configured via the Cloudinary dashboard.
      uploadPreset: 'tl0zsgze',
      // use different options to make it easier for the user to upload images
      sources: ["local", "url", "camera", "facebook", "dropbox", "instagram", "shutterstock", "google_drive", "unsplash", "getty"],
      // no need for advanced options
      showAdvancedOptions: false,
      // cropping enabled
      cropping: false,
      // no multiple image upload allowed
      multiple: false,
      defaultSource: "local",
      // todo: come back to finish the styling of this
      styles: {
        palette: {
          window: "#FFFFFF",
          windowBorder: "#90A0B3",
          tabIcon: "#0078FF",
          menuIcons: "#5A616A",
          textDark: "#000000",
          textLight: "#FFFFFF",
          link: "#0078FF",
          action: "#FF620C",
          inactiveTabIcon: "#0E2F5A",
          error: "#F44235",
          inProgress: "#0078FF",
          complete: "#20B832",
          sourceBg: "#E4EBF1"
        },
        fonts: {
          default: null,
          "'Fira Sans', sans-serif": {
            url: "https://fonts.googleapis.com/css?family=Fira+Sans",
            active: true
          }
        }
      }
    }, (error, result) => {
      if (!error && result && result.event === "success") {
        // log response
        console.log('Done! Here is the image info: ', result.info);
        // use the URL generated for the input value
        $('#recipeImageURL').val(result.info.secure_url);
        // display the uploaded image by setting the src of an img element
        $('#uploadedImage').attr('src', result.info.secure_url);
        // show uploaded image when the upload was successful
        $('#uploadedImage').show();
        // hide the upload button
        $('#upload_widget').hide();
        // change the text to reflect the status of the upload
        $("#uploadStatusText").text("Image uploaded successfully");
      } else {
        // if no image was uploaded, check if the #recipeImageURL input is empty
        if ($('#recipeImageURL').val() === '') {
          // if the #recipeImageURL input is empty, set the default image URL
          const defaultImageURL = 'https://i.ibb.co/kBz5npG/This-dish-disappeared-too-quickly-for-a-photoshoot.png';
          $('#recipeImageURL').val(defaultImageURL);
          $('#uploadedImage').attr('src', defaultImageURL);
          $('#uploadedImage').hide();

        }
      }
    });
  
    $('#upload_widget').on('click', function () {
      myWidget.open();
    });
  
    // hide the uploaded image element
    $('#uploadedImage').hide();
  });