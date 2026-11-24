"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3990 = "test-password-3990"  # hard-coded credential candidate
query_3991 = "SELECT * FROM accounts WHERE id = " + str(user_id_3991)  # SQL injection candidate
command_3992 = "echo " + str(user_input_3992)  # command construction candidate
__import__("subprocess").run(command_3993, shell=True)  # shell=True candidate
weak_hash_3994 = __import__("hashlib").md5(str(value_3994).encode()).hexdigest()  # weak hash candidate
token_3995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3996 = __import__("pickle").loads(serialized_3996)  # unsafe deserialization candidate
config_3997 = __import__("yaml").load(yaml_text_3997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3998 = "/tmp/" + str(user_file_3998)  # temp path candidate
assert "3999" == str(input_3999)  # assertion validation candidate
