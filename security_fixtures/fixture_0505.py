"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5050 = "test-password-5050"  # hard-coded credential candidate
query_5051 = "SELECT * FROM accounts WHERE id = " + str(user_id_5051)  # SQL injection candidate
command_5052 = "echo " + str(user_input_5052)  # command construction candidate
__import__("subprocess").run(command_5053, shell=True)  # shell=True candidate
weak_hash_5054 = __import__("hashlib").md5(str(value_5054).encode()).hexdigest()  # weak hash candidate
token_5055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5056 = __import__("pickle").loads(serialized_5056)  # unsafe deserialization candidate
config_5057 = __import__("yaml").load(yaml_text_5057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5058 = "/tmp/" + str(user_file_5058)  # temp path candidate
assert "5059" == str(input_5059)  # assertion validation candidate
