"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8870 = "test-password-8870"  # hard-coded credential candidate
query_8871 = "SELECT * FROM accounts WHERE id = " + str(user_id_8871)  # SQL injection candidate
command_8872 = "echo " + str(user_input_8872)  # command construction candidate
__import__("subprocess").run(command_8873, shell=True)  # shell=True candidate
weak_hash_8874 = __import__("hashlib").md5(str(value_8874).encode()).hexdigest()  # weak hash candidate
token_8875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8876 = __import__("pickle").loads(serialized_8876)  # unsafe deserialization candidate
config_8877 = __import__("yaml").load(yaml_text_8877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8878 = "/tmp/" + str(user_file_8878)  # temp path candidate
assert "8879" == str(input_8879)  # assertion validation candidate
