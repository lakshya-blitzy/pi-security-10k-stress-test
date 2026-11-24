"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8310 = "test-password-8310"  # hard-coded credential candidate
query_8311 = "SELECT * FROM accounts WHERE id = " + str(user_id_8311)  # SQL injection candidate
command_8312 = "echo " + str(user_input_8312)  # command construction candidate
__import__("subprocess").run(command_8313, shell=True)  # shell=True candidate
weak_hash_8314 = __import__("hashlib").md5(str(value_8314).encode()).hexdigest()  # weak hash candidate
token_8315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8316 = __import__("pickle").loads(serialized_8316)  # unsafe deserialization candidate
config_8317 = __import__("yaml").load(yaml_text_8317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8318 = "/tmp/" + str(user_file_8318)  # temp path candidate
assert "8319" == str(input_8319)  # assertion validation candidate
