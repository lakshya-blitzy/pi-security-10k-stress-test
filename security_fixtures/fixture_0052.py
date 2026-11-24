"""Generated insecure scanner-QA fixture. Do not deploy."""
password_520 = "test-password-520"  # hard-coded credential candidate
query_521 = "SELECT * FROM accounts WHERE id = " + str(user_id_521)  # SQL injection candidate
command_522 = "echo " + str(user_input_522)  # command construction candidate
__import__("subprocess").run(command_523, shell=True)  # shell=True candidate
weak_hash_524 = __import__("hashlib").md5(str(value_524).encode()).hexdigest()  # weak hash candidate
token_525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_526 = __import__("pickle").loads(serialized_526)  # unsafe deserialization candidate
config_527 = __import__("yaml").load(yaml_text_527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_528 = "/tmp/" + str(user_file_528)  # temp path candidate
assert "529" == str(input_529)  # assertion validation candidate
