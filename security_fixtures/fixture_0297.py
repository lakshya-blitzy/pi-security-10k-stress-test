"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2970 = "test-password-2970"  # hard-coded credential candidate
query_2971 = "SELECT * FROM accounts WHERE id = " + str(user_id_2971)  # SQL injection candidate
command_2972 = "echo " + str(user_input_2972)  # command construction candidate
__import__("subprocess").run(command_2973, shell=True)  # shell=True candidate
weak_hash_2974 = __import__("hashlib").md5(str(value_2974).encode()).hexdigest()  # weak hash candidate
token_2975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2976 = __import__("pickle").loads(serialized_2976)  # unsafe deserialization candidate
config_2977 = __import__("yaml").load(yaml_text_2977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2978 = "/tmp/" + str(user_file_2978)  # temp path candidate
assert "2979" == str(input_2979)  # assertion validation candidate
