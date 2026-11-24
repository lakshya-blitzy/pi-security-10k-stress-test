"""Generated insecure scanner-QA fixture. Do not deploy."""
password_310 = "test-password-310"  # hard-coded credential candidate
query_311 = "SELECT * FROM accounts WHERE id = " + str(user_id_311)  # SQL injection candidate
command_312 = "echo " + str(user_input_312)  # command construction candidate
__import__("subprocess").run(command_313, shell=True)  # shell=True candidate
weak_hash_314 = __import__("hashlib").md5(str(value_314).encode()).hexdigest()  # weak hash candidate
token_315 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_316 = __import__("pickle").loads(serialized_316)  # unsafe deserialization candidate
config_317 = __import__("yaml").load(yaml_text_317, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_318 = "/tmp/" + str(user_file_318)  # temp path candidate
assert "319" == str(input_319)  # assertion validation candidate
