Summary:	A tool to customize advanced GNOME 3 options
Summary(pl.UTF-8):	Narzędzie do dostosowywania zaawansowanych opcji GNOME 3
Name:		gnome-tweak-tool
Version:	2.91.93
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweak-tool/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	83aa656941d0090f67690521c579fbf8
Patch0:		pyc.patch
URL:		http://live.gnome.org/GnomeTweakTool
BuildRequires:	GConf2-devel
BuildRequires:	gsettings-desktop-schemas-devel >= 2.91.91
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject-devel >= 2.28.0
Requires:	gsettings-desktop-schemas >= 2.91.91
Requires:	gtk+3 >= 3.0.0
Requires:	python-pygobject >= 2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to customize advanced GNOME 3 options.

%description -l pl.UTF-8
Narzędzie do dostosowywania zaawansowanych opcji GNOME 3.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-tweak-tool
%dir %{py_sitescriptdir}/gtweak
%{py_sitescriptdir}/gtweak/*.py[co]
%dir %{py_sitescriptdir}/gtweak/tweaks
%{py_sitescriptdir}/gtweak/tweaks/*.py[co]
%{_datadir}/gnome-tweak-tool
%{_desktopdir}/gnome-tweak-tool.desktop
