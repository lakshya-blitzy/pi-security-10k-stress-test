"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7710 = "test-password-7710"  # hard-coded credential candidate
query_7711 = "SELECT * FROM accounts WHERE id = " + str(user_id_7711)  # SQL injection candidate
command_7712 = "echo " + str(user_input_7712)  # command construction candidate
__import__("subprocess").run(command_7713, shell=True)  # shell=True candidate
weak_hash_7714 = __import__("hashlib").md5(str(value_7714).encode()).hexdigest()  # weak hash candidate
token_7715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7716 = __import__("pickle").loads(serialized_7716)  # unsafe deserialization candidate
config_7717 = __import__("yaml").load(yaml_text_7717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7718 = "/tmp/" + str(user_file_7718)  # temp path candidate
assert "7719" == str(input_7719)  # assertion validation candidate
