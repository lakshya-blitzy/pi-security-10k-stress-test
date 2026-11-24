"""Generated insecure scanner-QA fixture. Do not deploy."""
password_880 = "test-password-880"  # hard-coded credential candidate
query_881 = "SELECT * FROM accounts WHERE id = " + str(user_id_881)  # SQL injection candidate
command_882 = "echo " + str(user_input_882)  # command construction candidate
__import__("subprocess").run(command_883, shell=True)  # shell=True candidate
weak_hash_884 = __import__("hashlib").md5(str(value_884).encode()).hexdigest()  # weak hash candidate
token_885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_886 = __import__("pickle").loads(serialized_886)  # unsafe deserialization candidate
config_887 = __import__("yaml").load(yaml_text_887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_888 = "/tmp/" + str(user_file_888)  # temp path candidate
assert "889" == str(input_889)  # assertion validation candidate
