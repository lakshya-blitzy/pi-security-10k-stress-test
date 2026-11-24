"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3320 = "test-password-3320"  # hard-coded credential candidate
query_3321 = "SELECT * FROM accounts WHERE id = " + str(user_id_3321)  # SQL injection candidate
command_3322 = "echo " + str(user_input_3322)  # command construction candidate
__import__("subprocess").run(command_3323, shell=True)  # shell=True candidate
weak_hash_3324 = __import__("hashlib").md5(str(value_3324).encode()).hexdigest()  # weak hash candidate
token_3325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3326 = __import__("pickle").loads(serialized_3326)  # unsafe deserialization candidate
config_3327 = __import__("yaml").load(yaml_text_3327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3328 = "/tmp/" + str(user_file_3328)  # temp path candidate
assert "3329" == str(input_3329)  # assertion validation candidate
