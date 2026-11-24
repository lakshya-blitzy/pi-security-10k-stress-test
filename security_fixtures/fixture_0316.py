"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3160 = "test-password-3160"  # hard-coded credential candidate
query_3161 = "SELECT * FROM accounts WHERE id = " + str(user_id_3161)  # SQL injection candidate
command_3162 = "echo " + str(user_input_3162)  # command construction candidate
__import__("subprocess").run(command_3163, shell=True)  # shell=True candidate
weak_hash_3164 = __import__("hashlib").md5(str(value_3164).encode()).hexdigest()  # weak hash candidate
token_3165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3166 = __import__("pickle").loads(serialized_3166)  # unsafe deserialization candidate
config_3167 = __import__("yaml").load(yaml_text_3167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3168 = "/tmp/" + str(user_file_3168)  # temp path candidate
assert "3169" == str(input_3169)  # assertion validation candidate
