"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3710 = "test-password-3710"  # hard-coded credential candidate
query_3711 = "SELECT * FROM accounts WHERE id = " + str(user_id_3711)  # SQL injection candidate
command_3712 = "echo " + str(user_input_3712)  # command construction candidate
__import__("subprocess").run(command_3713, shell=True)  # shell=True candidate
weak_hash_3714 = __import__("hashlib").md5(str(value_3714).encode()).hexdigest()  # weak hash candidate
token_3715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3716 = __import__("pickle").loads(serialized_3716)  # unsafe deserialization candidate
config_3717 = __import__("yaml").load(yaml_text_3717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3718 = "/tmp/" + str(user_file_3718)  # temp path candidate
assert "3719" == str(input_3719)  # assertion validation candidate
