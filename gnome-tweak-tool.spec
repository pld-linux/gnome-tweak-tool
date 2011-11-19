Summary:	A tool to customize advanced GNOME 3 options
Summary(pl.UTF-8):	Narzędzie do dostosowywania zaawansowanych opcji GNOME 3
Name:		gnome-tweak-tool
Version:	3.2.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tweak-tool/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	68680e451298b74684e3beb5c4169aaf
Patch0:		pyc.patch
URL:		http://live.gnome.org/GnomeTweakTool
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gsettings-desktop-schemas-devel >= 3.2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	GConf2-libs
Requires:	gobject-introspection
Requires:	gsettings-desktop-schemas >= 3.2.0
Requires:	gtk+3 >= 3.0.0
Requires:	python >= 1:2.6
Requires:	python-pygobject3 >= 3.0.0
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
