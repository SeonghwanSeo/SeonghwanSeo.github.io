// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "(*) indicates equal contribution",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "Last Updated: 2026.09.28",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-1-paper-is-accepted-to-tmlr-tacogfn",
          title: '1 paper is accepted to TMLR: TacoGFN',
          description: "",
          section: "News",},{id: "news-1-paper-is-accepted-to-neurips-2024-ai4drugx-workshop-rxnflow",
          title: '1 paper is accepted to NeurIPS 2024 AI4DrugX Workshop: RxnFlow',
          description: "",
          section: "News",},{id: "news-1-paper-is-accepted-to-chemical-science-pharmaconet",
          title: '1 paper is accepted to Chemical Science: PharmacoNet',
          description: "",
          section: "News",},{id: "news-1-paper-is-accepted-to-iclr-2025-rxnflow",
          title: '1 paper is accepted to ICLR 2025: RxnFlow',
          description: "",
          section: "News",},{id: "news-1-paper-is-accepted-as-spotlight-paper-to-iclr-2025-gem-and-ai4mat-workshop-cgflow",
          title: '1 paper is accepted as spotlight paper to ICLR 2025 GEM and AI4Mat...',
          description: "",
          section: "News",},{id: "news-hyper-screening-x-powered-by-rxnflow-has-became-a-world-s-largest-virtual-library-search-with-access-to-emolecules-11-trillion-compound-library-blog",
          title: 'Hyper Screening X powered by RxnFlow has became a world’s largest virtual library...',
          description: "",
          section: "News",},{id: "news-1-paper-is-accepted-to-icml-2025-cgflow",
          title: '1 paper is accepted to ICML 2025: CGFlow',
          description: "",
          section: "News",},{id: "news-2-papers-are-accepted-on-iclr-2026-gem-workshop-boltz2esi-and-af3-msd-af3-cluster",
          title: '2 papers are accepted on ICLR 2026 GEM Workshop: Boltz2ESi and AF3-MSD/AF3-Cluster.',
          description: "",
          section: "News",},{id: "news-i-organized-a-workshop-on-the-2026-workshop-on-generative-ai-and-agentic-ai-for-biology-genbio-at-icml-2026-seoul-korea",
          title: 'I organized a workshop on “The 2026 workshop on Generative AI and Agentic...',
          description: "",
          section: "News",},{id: "news-the-k-fold-preview-is-now-released",
          title: 'The K-Fold preview is now released.',
          description: "",
          section: "News",},{id: "projects-hyper-screening-x",
          title: 'Hyper Screening X',
          description: "Hyper Screening X utilizes RxnFlow to efficiently explore a 11-trillion-compound ultra-large library, identifying innovative drug candidates with low binding energy and over 85% synthetic feasibility.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%68%77%61%6E%30%31%30%36@%6B%61%69%73%74.%61%63.%6B%72", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/SeonghwanSeo", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/seonghwan-seo-5199b2251", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=NGc_Z_UAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
