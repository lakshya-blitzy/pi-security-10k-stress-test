"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3230 = "test-password-3230"  # hard-coded credential candidate
query_3231 = "SELECT * FROM accounts WHERE id = " + str(user_id_3231)  # SQL injection candidate
command_3232 = "echo " + str(user_input_3232)  # command construction candidate
__import__("subprocess").run(command_3233, shell=True)  # shell=True candidate
weak_hash_3234 = __import__("hashlib").md5(str(value_3234).encode()).hexdigest()  # weak hash candidate
token_3235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3236 = __import__("pickle").loads(serialized_3236)  # unsafe deserialization candidate
config_3237 = __import__("yaml").load(yaml_text_3237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3238 = "/tmp/" + str(user_file_3238)  # temp path candidate
assert "3239" == str(input_3239)  # assertion validation candidate
