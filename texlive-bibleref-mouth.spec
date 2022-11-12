Name:		texlive-bibleref-mouth
Version:	25527
Release:	1
Summary:	Consistent formatting of Bible references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-mouth
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.r25527.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.doc.r25527.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.source.r25527.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows Bible references to be formatted in a
consistent way. It is similar to the bibleref package, except
that the formatting macros are all purely expandable -- that
is, they are all implemented in TeX's mouth. This means that
they can be used in any expandable context, such as an argument
to a \url command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-mouth/bibleref-mouth.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-mouth/README
%doc %{_texmfdistdir}/doc/latex/bibleref-mouth/bibleref-mouth.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bibleref-mouth/bibleref-mouth.dtx
%doc %{_texmfdistdir}/source/latex/bibleref-mouth/bibleref-mouth.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
