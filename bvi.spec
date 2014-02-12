Summary:	A vi-like binary file editor
Name:		bvi
Version:	1.3.2
Release:	8
License:	GPLv2+
Group:		Editors
Url:		http://bvi.sourceforge.net/
Source0:	bvi-%{version}.tar.bz2
Patch0:		bvi-1.3.2-config.guess.patch.bz2
Patch1:		bvi-1.3.2-mdv-fix-str-fmt.patch
BuildRequires:	pkgconfig(ncurses)

%description
bvi is a display-oriented editor for binary files, based on the vi
text editor. If you are familiar with vi, just start the editor and
begin to edit! If you never heard about vi, maybe bvi is not the
best choice for you.

%files
%doc README COPYING CHANGES CREDITS
%{_bindir}/bvi
%{_bindir}/bmore
%{_bindir}/bview
%{_bindir}/bvedit
%{_mandir}/man1/bvi.1*
%{_mandir}/man1/bmore.1*
%{_mandir}/man1/bview.1*
%{_mandir}/man1/bvedit.1*
%{_datadir}/bmore.help

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .strfmt

find . -perm 0600 | xargs chmod 0644

%build
%configure2_5x --libdir=%{_datadir}
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}

install -m 755 bvi %{buildroot}%{_bindir}/bvi
install -m 755 bmore %{buildroot}%{_bindir}/bmore
install -m 644 bvi.1 %{buildroot}%{_mandir}/man1/bvi.1
install -m 644 bmore.1 %{buildroot}%{_mandir}/man1/bmore.1
install -m 644 bmore.help %{buildroot}%{_datadir}/bmore.help
ln -sf bvi %{buildroot}%{_bindir}/bview
ln -sf bvi %{buildroot}%{_bindir}/bvedit
echo ".so man1/bvi.1" > %{buildroot}%{_mandir}/man1/bview.1
echo ".so man1/bvi.1" > %{buildroot}%{_mandir}/man1/bvedit.1
chmod 644 README COPYING CHANGES CREDITS

