%define fontname thai-scalable
%define fontconf 90-%{fontname}-synthetic

%define archivename thaifonts-scalable

%define common_desc \
%{archivename} provides a collection of free scalable Thai fonts.

Name:      %{fontname}-fonts
Version:   0.4.12
Release:   2.1%{?dist}
Summary:   Thai TrueType fonts
Group:     User Interface/X
License:   GPLv2+
URL:       http://linux.thai.net/projects/thaifonts-scalable
Source0:   http://linux.thai.net/pub/ThaiLinux/software/%{archivename}/%{archivename}-%{version}.tar.gz
Source1:   %{fontconf}-garuda.conf
Source2:   %{fontconf}-kinnari.conf
Source3:   %{fontconf}-umpush.conf
BuildArch: noarch
BuildRequires: fontforge >= 20071110, ttmkfdir, xorg-x11-font-utils
BuildRequires: fontpackages-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
%common_desc

Thai scalable fonts included here are:
- Kinnari, Garuda and Norasi from the National Font project
- DB Thai Text from DearBook
- TlwgMono, PseudoMono, Purisa by TLWG


%package common
Summary:   Common files of <NAME>
Group:     User Interface/X
Requires:  fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


# added for F11 can be obsoleted for F13
%package compat
Summary:   thaifonts-scalable compatibility package
Group:     User Interface/X
Obsoletes: thaifonts-scalable < 0.4.11-1
Requires: %{fontname}-garuda-fonts
Requires: %{fontname}-kinnari-fonts
Requires: %{fontname}-loma-fonts
Requires: %{fontname}-norasi-fonts
Requires: %{fontname}-purisa-fonts
Requires: %{fontname}-sawasdee-fonts
Requires: %{fontname}-tlwgmono-fonts
Requires: %{fontname}-tlwgtypewriter-fonts
Requires: %{fontname}-tlwgtypist-fonts
Requires: %{fontname}-tlwgtypo-fonts
Requires: %{fontname}-umpush-fonts
Requires: %{fontname}-waree-fonts

%description compat
This package only exists to help transition thaifonts-scalable users to the new
split renamed package. It will be removed after one distribution release cycle,
please do not reference it or depend on it in any way.

It can be safely uninstalled.


%package -n %{fontname}-garuda-fonts
Summary:        Thai Garuda fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-garuda-fonts
%common_desc

This package provides the Garuda family of Thai fonts.

%_font_pkg -n garuda -f %{fontconf}-garuda.conf Garuda*.ttf


%package -n %{fontname}-kinnari-fonts
Summary:        Thai Kinnari fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-kinnari-fonts
%common_desc

This package provides the Kinnari family of Thai fonts.

%_font_pkg -n kinnari -f %{fontconf}-kinnari.conf Kinnari*.ttf


%package -n %{fontname}-loma-fonts
Summary:        Thai Loma fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-loma-fonts
%common_desc

This package provides the Loma family of Thai fonts.

%_font_pkg -n loma Loma*.ttf


%package -n %{fontname}-norasi-fonts
Summary:        Thai Norasi fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-norasi-fonts
%common_desc

This package provides the Norasi family of Thai fonts.

%_font_pkg -n norasi Norasi*.ttf


%package -n %{fontname}-purisa-fonts
Summary:        Thai Purisa fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-purisa-fonts
%common_desc

This package provides the Purisa family of Thai fonts.

%_font_pkg -n purisa Purisa*.ttf


%package -n %{fontname}-sawasdee-fonts
Summary:        Thai Sawasdee fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sawasdee-fonts
%common_desc

This package provides the Sawasdee family of Thai fonts.

%_font_pkg -n sawasdee Sawasdee*.ttf


%package -n %{fontname}-tlwgmono-fonts
Summary:        Thai TlwgMono fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgmono-fonts
%common_desc

This package provides the TlwgMono family of Thai fonts.

%_font_pkg -n tlwgmono TlwgMono*.ttf


%package -n %{fontname}-tlwgtypewriter-fonts
Summary:        Thai TlwgTypewriter fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypewriter-fonts
%common_desc

This package provides the TlwgTypewriter family of Thai fonts.

%_font_pkg -n tlwgtypewriter TlwgTypewriter*.ttf


%package -n %{fontname}-tlwgtypist-fonts
Summary:        Thai TlwgTypist fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypist-fonts
%common_desc

This package provides the TlwgTypist family of Thai fonts.

%_font_pkg -n tlwgtypist TlwgTypist*.ttf


%package -n %{fontname}-tlwgtypo-fonts
Summary:        Thai TlwgTypo fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypo-fonts
%common_desc

This package provides the TlwgTypo family of Thai fonts.

%_font_pkg -n tlwgtypo TlwgTypo*.ttf


%package -n %{fontname}-umpush-fonts
Summary:        Thai Umpush fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-umpush-fonts
%common_desc

This package provides the Umpush family of Thai fonts.

%_font_pkg -n umpush -f %{fontconf}-umpush.conf Umpush*.ttf


%package -n %{fontname}-waree-fonts
Summary:        Thai Waree fonts
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-waree-fonts
%common_desc

This package provides the Waree family of Thai fonts.

%_font_pkg -n waree Waree*.ttf


%prep
%setup -q -n %{archivename}-%{version}


%build
%configure --with-ttfdir=%{_fontdir} --enable-ttf=yes


%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove upstream font config
# fontconfig's 65-nonlatin.conf covers 65-ttf-thai-tlwg.conf
rm %{buildroot}%{_sysconfdir}/fonts/conf.avail/*-ttf-thai-tlwg*.conf

# split up 90-ttf-thai-tlwg-synthetic.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-garuda.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-kinnari.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-umpush.conf

for fconf in %{fontconf}-garuda.conf \
             %{fontconf}-kinnari.conf \
             %{fontconf}-umpush.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -rf $RPM_BUILD_ROOT


%files common
%defattr(-,root,root,-)
%doc AUTHORS README COPYING NEWS

%files compat
%defattr(-,root,root,-)
%{_fontdir}/fonts.dir
%{_fontdir}/fonts.scale


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4.12-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Jens Petersen <petersen@redhat.com> - 0.4.12-1
- update to 0.4.12 (reported by Manatsawin Hanmongkolchai in #507172)

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 0.4.11-3
— Make sure F11 font packages have been built with F11 fontforge

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Jens Petersen <petersen@redhat.com> - 0.4.11-1
- update to 0.4.11
- repackage and subpackage for new fontpackages-devel:
- split 90-ttf-thai-tlwg-synthetic.conf per subpackage
- 65-ttf-thai-tlwg.conf is covered by fontconfig 65-nonlatin.conf
- moves docs to common subpackage
- add compat subpackage for upgrades and legacy fonts.*

* Fri Feb  8 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-3
- couple more cleanups (Parag Nemade,#431829):
- use rm instead of /bin/rm
- use install -p

* Fri Feb  8 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-2
- add buildrequires for ttmkfdir and xorg-x11-font-utils (Parag Nemade,#431829)

* Wed Feb  6 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-1
- update to 0.4.9
- spec file cleanup

* Mon Jan 29 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.4.4-1
- Initial package based on package by Theppitak Karoonboonyanan
  and Kamthorn Krairaksa for the OLPC.
