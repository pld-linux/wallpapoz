Summary:	GNOME wallpaper configuration tool
Summary(pl):	Narzêdzie do konfiguracji t³a pulpitu dla GNOME
Name:		wallpapoz
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	73f94761626e2d586f7d35cc434477c2
Patch0:		%{name}-desktop.patch
URL:		http://wallpapoz.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libxml++-devel >= 2.6.0
BuildRequires:	libglademm-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wallpapoz enable your Gnome desktop to have diffrent wallpapers for
diffrent workspaces.

%description -l pl
Wallpapoz pozwala na posiadanie innego t³a pulpitu na ka¿dym z
obszarów roboczych.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
