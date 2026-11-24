"""Generated insecure scanner-QA fixture. Do not deploy."""
password_710 = "test-password-710"  # hard-coded credential candidate
query_711 = "SELECT * FROM accounts WHERE id = " + str(user_id_711)  # SQL injection candidate
command_712 = "echo " + str(user_input_712)  # command construction candidate
__import__("subprocess").run(command_713, shell=True)  # shell=True candidate
weak_hash_714 = __import__("hashlib").md5(str(value_714).encode()).hexdigest()  # weak hash candidate
token_715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_716 = __import__("pickle").loads(serialized_716)  # unsafe deserialization candidate
config_717 = __import__("yaml").load(yaml_text_717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_718 = "/tmp/" + str(user_file_718)  # temp path candidate
assert "719" == str(input_719)  # assertion validation candidate
