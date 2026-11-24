"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2340 = "test-password-2340"  # hard-coded credential candidate
query_2341 = "SELECT * FROM accounts WHERE id = " + str(user_id_2341)  # SQL injection candidate
command_2342 = "echo " + str(user_input_2342)  # command construction candidate
__import__("subprocess").run(command_2343, shell=True)  # shell=True candidate
weak_hash_2344 = __import__("hashlib").md5(str(value_2344).encode()).hexdigest()  # weak hash candidate
token_2345 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2346 = __import__("pickle").loads(serialized_2346)  # unsafe deserialization candidate
config_2347 = __import__("yaml").load(yaml_text_2347, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2348 = "/tmp/" + str(user_file_2348)  # temp path candidate
assert "2349" == str(input_2349)  # assertion validation candidate
