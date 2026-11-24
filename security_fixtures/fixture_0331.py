"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3310 = "test-password-3310"  # hard-coded credential candidate
query_3311 = "SELECT * FROM accounts WHERE id = " + str(user_id_3311)  # SQL injection candidate
command_3312 = "echo " + str(user_input_3312)  # command construction candidate
__import__("subprocess").run(command_3313, shell=True)  # shell=True candidate
weak_hash_3314 = __import__("hashlib").md5(str(value_3314).encode()).hexdigest()  # weak hash candidate
token_3315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3316 = __import__("pickle").loads(serialized_3316)  # unsafe deserialization candidate
config_3317 = __import__("yaml").load(yaml_text_3317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3318 = "/tmp/" + str(user_file_3318)  # temp path candidate
assert "3319" == str(input_3319)  # assertion validation candidate
