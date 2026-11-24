"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2990 = "test-password-2990"  # hard-coded credential candidate
query_2991 = "SELECT * FROM accounts WHERE id = " + str(user_id_2991)  # SQL injection candidate
command_2992 = "echo " + str(user_input_2992)  # command construction candidate
__import__("subprocess").run(command_2993, shell=True)  # shell=True candidate
weak_hash_2994 = __import__("hashlib").md5(str(value_2994).encode()).hexdigest()  # weak hash candidate
token_2995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2996 = __import__("pickle").loads(serialized_2996)  # unsafe deserialization candidate
config_2997 = __import__("yaml").load(yaml_text_2997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2998 = "/tmp/" + str(user_file_2998)  # temp path candidate
assert "2999" == str(input_2999)  # assertion validation candidate
