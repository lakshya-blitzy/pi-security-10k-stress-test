"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3010 = "test-password-3010"  # hard-coded credential candidate
query_3011 = "SELECT * FROM accounts WHERE id = " + str(user_id_3011)  # SQL injection candidate
command_3012 = "echo " + str(user_input_3012)  # command construction candidate
__import__("subprocess").run(command_3013, shell=True)  # shell=True candidate
weak_hash_3014 = __import__("hashlib").md5(str(value_3014).encode()).hexdigest()  # weak hash candidate
token_3015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3016 = __import__("pickle").loads(serialized_3016)  # unsafe deserialization candidate
config_3017 = __import__("yaml").load(yaml_text_3017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3018 = "/tmp/" + str(user_file_3018)  # temp path candidate
assert "3019" == str(input_3019)  # assertion validation candidate
