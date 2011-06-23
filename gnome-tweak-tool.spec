Summary:	A tool to customize advanced GNOME 3 options
Summary(pl.UTF-8):	Narzędzie do dostosowywania zaawansowanych opcji GNOME 3
Name:		gnome-tweak-tool
Version:	3.0.5
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweak-tool/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	a3595f33636f19eb319087562a9a5105
Patch0:		pyc.patch
URL:		http://live.gnome.org/GnomeTweakTool
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gsettings-desktop-schemas-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-pygobject-devel >= 2.28.0
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	gsettings-desktop-schemas >= 3.0.0
Requires:	gtk+3 >= 3.0.0
Requires:	python >= 1:2.6
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-tweak-tool
%dir %{py_sitescriptdir}/gtweak
%{py_sitescriptdir}/gtweak/*.py[co]
%dir %{py_sitescriptdir}/gtweak/tweaks
%{py_sitescriptdir}/gtweak/tweaks/*.py[co]
%{_datadir}/gnome-tweak-tool
%{_desktopdir}/gnome-tweak-tool.desktop
