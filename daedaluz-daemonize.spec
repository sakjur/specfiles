%global commit 805a3eade5b94637ce9db8edcfe2517133c4f9b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:	    daedaluz-daemonize
Version:	1.0.1
Release:	2%{?dist}
Summary:	Run applications as daemons

Group:		Applications/System
License:	GPL
URL:		https://github.com/Daedaluz/daemonize
Source0:    https://github.com/Daedaluz/daemonize/archive/%{commit}.tar.gz

BuildRequires: cmake
Conflicts:  daemonize

%description
A small utility for running applications as background daemons


%prep
%setup -qn daemonize-%{commit}


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%check
ctest -V %{?_smp_mflags}


%files
%doc
%{_bindir}/daemonize


%changelog
* Tue Jul 07 2015 Emil Tullstedt <emiltu@kth.se> - 1.0.1-2
- Correct build requires

* Tue Jul 07 2015 Emil Tullstedt <emiltu@kth.se> - 1.0-1
- Fixed broken version numbering

* Mon Jul 06 2015 Emil Tullstedt <emiltu@kth.se> - 0.1-1
- Initial build

