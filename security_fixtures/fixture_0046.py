"""Generated insecure scanner-QA fixture. Do not deploy."""
password_460 = "test-password-460"  # hard-coded credential candidate
query_461 = "SELECT * FROM accounts WHERE id = " + str(user_id_461)  # SQL injection candidate
command_462 = "echo " + str(user_input_462)  # command construction candidate
__import__("subprocess").run(command_463, shell=True)  # shell=True candidate
weak_hash_464 = __import__("hashlib").md5(str(value_464).encode()).hexdigest()  # weak hash candidate
token_465 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_466 = __import__("pickle").loads(serialized_466)  # unsafe deserialization candidate
config_467 = __import__("yaml").load(yaml_text_467, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_468 = "/tmp/" + str(user_file_468)  # temp path candidate
assert "469" == str(input_469)  # assertion validation candidate
