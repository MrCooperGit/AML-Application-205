function openTab(pageName, url) {
    console.log(`Opening tab: ${pageName}, URL: ${url}`);
  
    // Check if the tab is already open
    var existingTab = document.getElementById(`${pageName}-tab`);
  
    // Replace spaces and parentheses with underscores
    var validPageName = pageName.replace(/[ ()]/g, "_");
  
    if (!existingTab) {
      // Create a new tab
      var tabLink = document.createElement("li");
      tabLink.innerHTML = `
          <a class="nav-link text-decoration-none" id="${validPageName}-tab" data-bs-toggle="pill" href="#${pageName}" onclick="loadContent('${pageName}', '${url}')">
            ${pageName}
            <button type="button" class="btn-close" aria-label="Close" onclick="closeTab('${pageName}')"></button>
          </a>
        `;
      tabLink.classList.add("nav-item");
      tabLink.id = `${pageName}-tab`;
      document.getElementById("tabsList").appendChild(tabLink);
  
      // Load content for the tab
      loadContent(pageName, url);
    } else {
      // If the tab already exists, find a suitable name
      var i = 2;
      var modifiedPageName = `${pageName}-${i}`;
      while (document.getElementById(`${modifiedPageName}-tab`)) {
        i++;
        modifiedPageName = `${pageName}-${i}`;
      }
      // Log the ID of the created tab
      console.log(`Created tab with ID: ${modifiedPageName}-tab`);
  
      // Create a new tab with the modified name
      openTab(modifiedPageName, url);
    }
  }
  
  function openTabAndSave(pageName, element, url) {
    // Save form data for the current page
    var currentPage = $(".sidebar-link.active").text().trim();
    // Remove existinf data for current page
    localStorage.removeItem(currentPage);
    console.log("Current Page for save (sidebar):", currentPage);
    saveFormData(currentPage);
  
    // Remove 'active' class from all sidebar links
    $(".sidebar-link").removeClass("active");
  
    // Add 'active' class to the clicked link
    $(element).addClass("active");
    var classes = element.classList;
  
    if (classes.contains("active")) {
      console.log(element, "Element has the 'active' class");
    } else {
      console.log("Element does not have the 'active' class");
    }
  
    openTab(pageName, url);
  }
  
  // Function to save form data to localStorage
  function saveFormData(pageName) {
    var formData = {};
  
    // Iterate through all form elements within the identified form
    $(`form[data-page="${pageName}"] :input`).each(function () {
      var element = $(this);
      var fieldName = element.attr("name");
  
      // Check if the field is a date field
      if (element.attr("type") === "date") {
        // Format the date field value to "yyyy-MM-dd"
        var dateValue = element.val();
        if (dateValue) {
          formData[fieldName] = dateValue;
        } else {
          formData[fieldName] = null;
        }
      }
    });
  
    // Store the form data in localStorage
    localStorage.setItem(pageName, JSON.stringify(formData));
  
    // Log the saved data
    console.log(`Saved data for ${pageName}:`, formData);
  
    // Check if the data is actually stored in localStorage
    var storedData = localStorage.getItem(pageName);
    console.log(`Data stored in localStorage for ${pageName}:`, storedData);
  }
  
  // Function to load form data from localStorage
  function loadFormData(pageName) {
    // Retrieve the form data from localStorage
    var storedData = localStorage.getItem(pageName);
    console.log(`Attempting to load data for ${pageName}. Stored data:`, storedData);
  
    if (storedData) {
      // Parse the stored data and populate the form
      var formData = JSON.parse(storedData);
  
      // Log the loaded data
      console.log(`Loaded data for ${pageName}:`, formData);
  
      // Identify the form based on the data-page attribute
      var formSelector = `form[data-page="${pageName}"]`;
  
      // Iterate through all form elements
      $(formSelector + " :input").each(function () {
        var element = $(this);
        var fieldName = element.attr("name");
  
        // Update fieldName to match Django's naming convention
        fieldName = "id_" + fieldName;
  
        console.log("Element:", element);
        console.log("Field Name:", fieldName);
        console.log("Stored Value:", formData[fieldName]);
        console.log("Element Value:", element.val());
  
        if (fieldName && formData.hasOwnProperty(fieldName)) {
          // Populate the field with the stored value
          element.val(formData[fieldName]);
        }
      });
    }
  }
  
  // Call saveFormData when leaving the tab
  $(document).on("hide.bs.tab", ".nav-link", function () {
    $(".sidebar-link").removeClass("active");
    var currentPage = $(".active").text().trim();
    console.log("Current Page for save:", currentPage);
    saveFormData(currentPage);
  });
  
  // Call loadFormData when switching to a tab
  $(document).on("shown.bs.tab", ".nav-link", function () {
    var targetPage = $(this).text().trim();
    loadFormData(targetPage);
  });
  
  function loadContent(pageName, url) {
    // Fetch content using AJAX
    $.get(url, function (data) {
      console.log("Fetched Data:", data);
  
      // Extract content within the body tags
      var bodyContent = data.match(/<body[^>]*>[\s\S]*<\/body>/gi);
      var bodyElement = document.createElement("div");
      bodyElement.innerHTML = bodyContent ? bodyContent[0] : data;
  
      //console.log("Body Element:", bodyElement);
  
      // Check if there are scripts in the body
      if (bodyElement) {
        // Insert the fetched content into the tab
        var contentContainer = document.getElementById("contentContainer");
        contentContainer.innerHTML = `<div id="${pageName}">${bodyElement.innerHTML}</div>`;
  
        // Append scripts to the contentContainer
        var bodyScripts = bodyElement.querySelectorAll("script");
        console.log("Page Name:", pageName);
        console.log("URL:", url);
        console.log("Body Scripts:", bodyScripts);
  
        var scriptsToExecute = [];
        if (bodyScripts.length > 0) {
          bodyScripts.forEach(function (script) {
            console.log("Appending Script:", script);
            var scriptClone = document.createElement("script");
            scriptClone.type = script.type || "text/javascript";
            scriptClone.text = script.innerHTML;
            contentContainer.appendChild(scriptClone);
  
          // Collect scripts for later execution
          scriptsToExecute.push(scriptClone);
          });
        // Manually execute all the collected scripts
        scriptsToExecute.forEach(function (script) {
            eval(script.text);
        });
        }
      } else {
        console.error("No body element found in the fetched content.");
      }
    });
  }
          

    function closeTab(pageName) {
    // Check if the tab and its content exist
    var tabElement = document.getElementById(`${pageName}-tab`);
    var contentElement = document.getElementById(`${pageName}`);
  
    if (tabElement) {
      // Remove the tab and its content
      console.log(`Closing tab: ${pageName}`);
      tabElement.remove();
    } else {
      console.log(`Tab not found for: ${pageName}`);
    }
  
    if (contentElement) {
      // Remove the tab and its content
      console.log(`Closing tab content: ${pageName}`);
      contentElement.remove();
    } else {
      console.log(`Content not found for: ${pageName}`);
    }
  
    // Check if there are no more tabs
    var remainingTabs = $("#tabsList li").length;
    if (remainingTabs === 0) {
      console.log("No more tabs. Redirecting to /landing");
      // Set the URL back to /cdd/
      window.location.href = "/landing";
    } else {
      console.log(`Tabs still open. Remaining tabs: ${remainingTabs}`);
    }
  }
  
//Open the link in new tab
var pdfUrl = "/risk/risk-pdf";
function openInNewTabButton() {
    console.log("click activated");
    window.open(pdfUrl, "_blank");
};
