%global _texmf %{_datadir}/texlive/texmf-local

Name:       inmallar
Version:    0.3
Release:    1%{?dist}
Summary:    Templates for internal usage within IN-sektionen at KTH

Group:      Applications/Publishing
License:    Proprietary
URL:        http://www.insektionen.se
Source0:    %{name}-%{version}.tar.xz
Requires:   tex(latex)
Requires(post): kpathsea
Requires(postun): kpathsea

%description
Templates for internal usage within the chapter for Information- and
Nanotechnology within the THS student body at the Royal Institute of
Technology in Stockholm. Super not useful anywhere else.

%prep
%setup -q


%build
# -- Skipping: This is not a binary package --


%install
%make_install

%post -p /usr/bin/mktexlsr

%postun -p /usr/bin/mktexlsr

%files
%{_texmf}/tex/latex/inmallar/

%changelog
* Mon Jul 06 2015 Emil Tullstedt <emiltu@kth.se> - 0.3-1
- Initial build 
