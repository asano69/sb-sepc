# Bootstrapの設計思想にアプリ全体が依存

典型的なBootstrap3 アプリの成長パターン


## 1. グリッドシステム依存


```css
.col-xs-1
.col-xs-2
...
.col-sm-*
.col-md-*
.col-lg-*
```

Bootstrap3のレイアウトは以下が前提

```html
<div class="row">
  <div class="col-md-8">
  <div class="col-md-4">
</div>
```

つまりUI設計が以下に結びつく

```text
12カラム
row
col-md-*
```

今なら普通は

```css
display: grid;
```

や

```css
display: flex;
```

で作る。

しかしアプリ全体に

```html
col-md-*
```

が数千箇所あると、

```text
Bootstrap除去
↓
全ページ崩壊
```

になる。これが最大級の技術負債。



## 2. Navbar依存

大量にある。

```css
.navbar
.navbar-default
.navbar-inverse
.navbar-toggle
.navbar-brand
.navbar-nav
```

Bootstrap3では

```html
<nav class="navbar navbar-default">
```

が標準。問題は、アプリ固有のナビゲーションも

```css
.navbar-common
.navbar-skeleton
```

になっていること。つまり

```text
Bootstrap Navbar
↓
アプリ独自Navbar
↓
CSS継承
```

になっている。Bootstrapを抜くとすべて壊れる

## 3. Buttonシステム依存

```css
.btn
.btn-primary
.btn-danger
.btn-warning
.btn-success
```

```css
.new-button
.file-upload-btn
```

もある。多くの画面で

```html
<button class="btn btn-primary">
```

が前提になっているはず。つまり

```text
Bootstrap Button API
↓
業務ロジック
```

が密結合。


## 4. Modal依存

```css
.modal
.modal-dialog
.modal-content
.modal-header
.modal-body
.modal-footer
```

さらに

```css
.draw-modal
.embed-text-modal
.file-upload-modal
.smart-context-modal
```

もある。つまり独自機能が全部

```html
<div class="modal">
```

前提。Bootstrap Modal を置き換えると

```text
全ダイアログ再実装
```

になる。


## 5. Form依存

大量。

```css
.form-control
.form-group
.form-horizontal
.has-error
.has-warning
.has-success
```
Bootstrap3は

```html
<div class="form-group">
  <input class="form-control">
</div>
```

文化。今なら

```css
input {}
.error {}
```

みたいに書くが、Bootstrap3時代は

```text
form-group
form-control
help-block
```

が必須。だから移行が重い。


## 6. Panel依存

これが年代を感じる。

```css
.panel
.panel-heading
.panel-body
.panel-footer

.panel-primary
.panel-info
.panel-danger
```



Bootstrap4で消滅したコンポーネント。つまりこのコードベースは

```text
Bootstrap4
↓
Bootstrap5
```

への移行をほぼ経験していない。

## 7. Visibility Utility

```css
.visible-xs
.visible-sm
.visible-md
.visible-lg
```
Bootstrap3特有。Bootstrap5なら

```css
.d-none
.d-md-block
```

になる。このクラスが大量にあると、移行時に全部書き換え。


## 8. Dropdown依存

```css
.dropdown
.dropdown-menu
.dropdown-toggle
```

さらに

```css
.page-menu
.popup-menu
.user-menu
```

がある。つまり独自メニューがBootstrap Dropdownの上に乗っている。



## 逆に技術負債ではない部分

比較的新しい独自コンポーネント。

```css
.smart-context-modal
.shared-cursors
.page-history
.related-page-list
.updatable-map
.project-metrics
```

これらは単なる業務ドメインのクラス。
Bootstrapを捨てても残る。
なのでこのCSSを見たときに一番強い技術負債は、

```text
Grid (.row .col-*)
Navbar
Button
Modal
Form
Panel
Visibility Utility
Dropdown
```

の8系統です。特に

```text
col-xs-*
col-sm-*
col-md-*
col-lg-*
```

が大量に残っている時点で、「Bootstrap3のレイアウトモデルにアプリ全体がロックインされている」というのが最も大きな負債だと考えられます。
