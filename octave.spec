Summary:	GNU Octave -- a high-level language for numerical computations
Summary(pl):	GNU Octave -- jêzyk programowania do obliczeñ numerycznych
Name:		octave
Version:	2.1.33
Release:	3
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://ftp.che.wisc.edu/pub/octave/%{name}-%{version}.tar.bz2
Patch0:		%{name}-liboctave.info.patch
Patch1:		%{name}-Octave-FAQ.info.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://www.che.wisc.edu/octave/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gcc-g77
Requires:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description -l pl
GNU Octave jest jêzykiem programowania wysokiego poziomu przeznaczonym
g³ównie do obliczeñ numerycznych. Octave jest w du¿ym stopniu
kompatybilny z jêzykiem Matlab. Pracowaæ mo¿na wprost z linii poleceñ
lub uruchamiaæ programy stworzone za pomoc± zewnêtrznego edytora.

%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):	Pliki nag³ówkowe i dodatkowa dokumentacja Octave 
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and devel docs for Octave.

%description -l pl devel
Pliki nag³ówkowe i dodatkowa dokumentacja Octave.

%package -n xemacs-octave-mode-pkg
Summary:	XEmacs mode for Octave
Summary(pl):	Tryb edycji plików Octave dla XEmacsa 
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	xemacs

%description -n xemacs-octave-mode-pkg
XEmacs mode for Octave.

%description -l pl -n xemacs-octave-mode-pkg
Tryb edycji plików Octave dla XEmacsa.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%configure2_13 \
	--with-g77 \
	--enable-dl \
	--enable-shared \
	--enable-rpath \
	--enable-lite-kernel

%{__make} 
%{__make} -C doc/faq Octave-FAQ.info
%{__make} -C doc/liboctave liboctave.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install doc/liboctave/*.info* $RPM_BUILD_ROOT%{_infodir}
install doc/faq/*.info* $RPM_BUILD_ROOT%{_infodir}

## xemacs-octave-mode-pkg
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
cp -a emacs/*.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
# add otags script or not (additional Requires: ctags)???
#cp -a emacs/otags $RPM_BUILD_ROOT%{_bindir}
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode/auto-autoloads.el
(autoload 'run-octave "octave-inf" nil t)
(autoload 'octave-help "octave-hlp" nil t)
(autoload 'octave-mode "octave-mod" nil t)
(setq auto-mode-alist
      (cons '("\\\\.m$" . octave-mode) auto-mode-alist))
EOF

gzip -9nf ChangeLog NEWS THANKS PROJECTS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz emacs examples doc/{interpreter,faq}/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_infodir}/octave.info*
%{_infodir}/Octave-FAQ.info*
%{_mandir}/man1/*
%{_datadir}/octave

%files devel
%defattr(644,root,root,755)
%doc doc/refcard/refcard{-a4,}.* doc/liboctave/*.html
%{_includedir}/%{name}
%{_infodir}/liboctave.info*

%files -n xemacs-octave-mode-pkg
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*
    
